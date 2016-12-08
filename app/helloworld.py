# -*- coding: utf-8 -*-
import json
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)




@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/post')
def post():
   customer = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
   decode_test = json.loads(customer)
   print(decode_test['name'])
   return render_template('post.html',  json_string = decode_test['name'])

@app.route('/contact')
def contact():
   return render_template('contact.html')


if __name__ == '__main__':
   app.run()
