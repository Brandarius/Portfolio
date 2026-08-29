import flask
from flask import render_template, redirect, url_for


app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run()
