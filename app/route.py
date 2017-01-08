# -*- coding: utf-8 -*-
import json, uuid
from flask import Flask, redirect, url_for, request, render_template
from MysqlDAO import MysqlDAO
from app import apiRoute
import datetime


app = Flask(__name__)
# register api router
app.register_blueprint(apiRoute.api)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/photo')
def about():
   return render_template('photo.html')

@app.route('/posts', methods=['GET'])
def post():
    var = MysqlDAO.post_select()
    print(var)
    return render_template('post.html', posts=var)

@app.route("/posts/<uuid>")
def updateDeletPost():
   request.__getattr__("uuid")

@app.route('/contact')
def contact():
   return render_template('contact.html')

def run():
    print("Cupid Start at %s"%str(datetime.datetime.now()))
    app.run(host="0.0.0.0", port=int("80"), debug=True)