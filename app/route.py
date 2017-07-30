
# -*- coding: utf-8 -*-
import json, uuid, os
from flask import Flask, redirect, url_for, request, render_template, send_from_directory
from MysqlDAO import MysqlDAO
from app import apiRoute
import datetime
from werkzeug import secure_filename
from config import *


app = Flask(__name__)
# register api router
app.register_blueprint(apiRoute.api)

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/photo', methods=['POST', 'GET', 'PUT'])
def photo():
   if request.method == "POST":
        f = request.files['file']
        photoname = MysqlDAO.photo_upload(f.filename)
        # app.config['UPLOAD_FOLDER'] = PHOTO_PATH
        f.save(os.path.join(PHOTO_PATH ,secure_filename(photoname)))
        return redirect("/photo", code=302)


   elif request.method == "GET":
        # path = {"static/img/IMG_2783"}
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

@app.route('/post', methods=['GET', 'POST'])
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
        #fileDAO.modify(updateObj)
        return ""

    elif request.method == "DELETE" :
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
    print("Cupid Start at %s"%str(datetime.datetime.now()))
    app.run(host="0.0.0.0", port=int("18080"), debug=True, threaded=True)
