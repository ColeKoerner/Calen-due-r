from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template('routes/calendar.html')

@app.route('/todolist')
def todolist():
    return render_template('routes/todolist.html')