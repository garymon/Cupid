# -*- coding: utf-8 -*-
import json, uuid, os
from flask import Flask, redirect, url_for, request, render_template, send_from_directory, session
from MysqlDAO import MysqlDAO
from app import apiRoute
import datetime
from werkzeug import secure_filename
from config import *
from oauth2client import client
import httplib2
from apiclient import discovery

app = Flask(__name__)
# register api router
app.register_blueprint(apiRoute.api)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    if 'user_info' not in session:
        return render_template("login.html")
    else:
        return redirect(url_for('index'))

@app.route('/oauth2/google')
def login_with_google():
    if 'credentials' not in session:
        return redirect(url_for('oauth_callback'))
    credentials = client.OAuth2Credentials.from_json(session['credentials'])
    if credentials.access_token_expired:
        return redirect(url_for('oauth_callback'))
    else:
        user_info_service = discovery.build(
            serviceName='oauth2', version='v2',
            http=credentials.authorize(httplib2.Http()))
        user_info = None
        try:
            user_info = user_info_service.userinfo().get().execute()
            session['user_info'] = user_info
            session.modified = True
        except Exception as e:
            print('An error occurred: {0}'.format(str(e)))
        print(user_info)
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'user_info' not in session:
        return redirect(url_for('index'))
    session.clear()
    return redirect(url_for('index'))


@app.route('/oauth2/google/callback')
def oauth_callback():
    flow = client.flow_from_clientsecrets('client_secrets.json',
                                          scope='https://www.googleapis.com/auth/userinfo.profile',
                                          redirect_uri=url_for('oauth_callback', _external=True))
    if 'code' not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        session['credentials'] = credentials.to_json()
        return redirect(url_for('login_with_google'))


@app.route('/photo', methods=['POST', 'GET', 'PUT'])
def photo():
    if request.method == "POST":
        print("photo() POST")
        f = request.files['file']
        print(f)
        photoname = MysqlDAO.photo_upload(f.filename)
        print(photoname)
        # app.config['UPLOAD_FOLDER'] = PHOTO_PATH
        f.save(os.path.join(PHOTO_PATH, secure_filename(photoname)))
        return redirect("/photo", code=302)

    elif request.method == "GET":
        # path = {"static/img/\IMG_2783"}
        DBphoto = MysqlDAO.photo_select()
        print(DBphoto)
        return render_template('photo.html', photos=DBphoto)

    elif request.method == "PUT":
        return render_template('photo.html')


@app.route('/photo/<uuid>', methods=['GET'])
def get_photo(uuid):
    if request.method == "GET":
        DBphoto = MysqlDAO.get_photo(uuid)
        # flask return image
        return send_from_directory(PHOTO_PATH, DBphoto['uuid'])


@app.route('/post', methods=['GET', 'PUT', 'POST', 'DELETE'])
def post():
    #     var = MysqlDAO.post_select()
    if request.method == "GET":
        var = MysqlDAO.post_select()
        return render_template('post.html', posts=var)

    elif request.method == "POST":
        insertObj = request.get_json()
        MysqlDAO.post_insert(insertObj)
        return ""

    elif request.method == "PUT":
        updateObj = request.get_json()
        MysqlDAO.post_update(updateObj)
        # fileDAO.modify(updateObj)
        return ""

    elif request.method == "DELETE":
        removeObj = request.get_json()
        MysqlDAO.post_delete(removeObj)
        return ""


# @app.route("/posts/<uuid>")
# def updateDeletPost():
#    request.__getattr__("uuid")


@app.route('/contact')
def contact():
    return render_template('contact.html')


def run():
    print("Cupid Start at %s" % str(datetime.datetime.now()))
    app.secret_key = str(uuid.uuid4())
    app.run(host="0.0.0.0", port=int("18080"), debug=True, threaded=True)
