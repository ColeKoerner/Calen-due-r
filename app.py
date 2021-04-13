from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = 5000, debug = True)