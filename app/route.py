# -*- coding: utf-8 -*-
import json, uuid
from flask import Flask, redirect, url_for, request, render_template
from MysqlDAO import MysqlDAO

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/photo')
def about():
   return render_template('photo.html')

@app.route('/posts', methods=['POST', 'GET', 'PUT', 'DELETE'])
def post():
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

@app.route("/posts/<uuid>")
def updateDeletPost():
   request.__getattr__("uuid")

@app.route('/contact')
def contact():
   return render_template('contact.html')

def run():

    app.run()