from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   print("aa")
   return render_template('index.html' )

@app.route('/success')
def success():
   return render_template('success.html', name = request.args.get('name'))


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
if __name__ == '__main__':
   app.run()