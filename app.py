from flask import Flask, jsonify, render_template, redirect, url_for

DEBUG = True

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')