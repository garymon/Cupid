# -*- coding: utf-8 -*-
import json, uuid
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)




@app.route('/')
def index():
   return render_template('index.html')

def jsonController(myData) :
   myData['uuid'] = str(uuid.uuid4())

   fRead = open("post.json", 'r')
   originJson= fRead.read()
   fRead.close()

   if not originJson :
       originJson = "[]"

   fWrite = open("post.json", 'w')

   originDataArr = json.loads(originJson)

   originDataArr.append(myData)

   fWrite.write(json.dumps(originDataArr))
   fWrite.close()


@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/posts', methods=['POST', 'GET'])
def post():
   if request.method == "GET":
      fRead = open("post.json", 'r')
      outputJson = fRead.read()
      fRead.close()
      if not outputJson :
         return render_template('post.html')
      outputJson = json.loads(outputJson)
      outputJson.reverse()
      return render_template('post.html', posts=outputJson)

   elif request.method == "POST":
      req_json = request.get_json()
      jsonController(req_json)
      return render_template('post_template.html', posts=[req_json])

@app.route('/contact')
def contact():
   return render_template('contact.html')


if __name__ == '__main__':
   app.run()
