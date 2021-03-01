import webbrowser
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return 'Welcome to home page'


@app.route('/second/<name>')
def second(name):
    return f"hello{name}"


@app.route('/Admin')
def admin():
    return 'Welcome to admin page'


@app.route('/a')
# webbrowser.open_new_tab('http://mylink.com')
def fb():
    return webbrowser.open_new_tab('http://www.facebook.com')


@app.route('/print/<int:number>')
def p(number):
    return render_template("index.html", marks=number)
    #


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %2f' % revNo


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('Admin'))
   else:
      return redirect(url_for('second',name = name))


app.run(debug=True)
