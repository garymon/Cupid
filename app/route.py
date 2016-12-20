# -*- coding: utf-8 -*-
import json, uuid
from flask import Flask, redirect, url_for, request, render_template
from FileDAO import fileDAO

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/posts', methods=['POST', 'GET', 'PUT', 'DELETE'])
def post():
   if request.method == "GET":
        return render_template('post.html', posts=fileDAO.get_all_posts())

   elif request.method == "POST":
        insertObj = request.get_json()
        fileDAO.save(insertObj)
        return ""

   elif request.method == "PUT":
        updateObj = request.get_json()
        fileDAO.modify(updateObj)
        return ""

   elif request.method == "DELETE" :
        removeObj = request.get_json()
        fileDAO.remove(removeObj)
        return ""

@app.route("/posts/<uuid>")
def updateDeletPost():
   request.__getattr__("uuid")

@app.route('/contact')
def contact():
   return render_template('contact.html')

def run():

    app.run()