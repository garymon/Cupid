# -*- coding: utf-8 -*-
import json, uuid, os
from flask import Flask, redirect, url_for, request, render_template
from MysqlDAO import MysqlDAO
from app import apiRoute
import datetime
from werkzeug import secure_filename


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
        photoname = f.filename
        MysqlDAO.photo_upload(f, photoname)
        UPLOAD_FOLDER = '../Cupid/app/static/img/imgpost'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return render_template('photo.html')

   elif request.method == "GET":
        # path = {"static/img/IMG_2783.JPG"}
        var = MysqlDAO.photo_select()
        print(var)
        return render_template('photo.html', photos=var)

   elif request.method == "PUT":
        return render_template('photo.html')

@app.route('/posts', methods=['GET'])
def post():
    var = MysqlDAO.post_select()

    if request.method == "GET":
        var = MysqlDAO.post_select()
        print(var)
        return render_template('post.html', posts=var)

    elif request.method == "POST":
        insertObj = request.get_json()
        MysqlDAO.post_insert(insertObj)
        #fileDAO.save(insertObj)
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
"""
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        print(secure_filename(f.filename))
        f.save(secure_filename(f.filename))
        return render_template('photo.html')
"""

@app.route("/posts/<uuid>")
def updateDeletPost():
   request.__getattr__("uuid")

@app.route('/contact')
def contact():
   return render_template('contact.html')

def run():
    print("Cupid Start at %s"%str(datetime.datetime.now()))
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
