from flask import render_template, flash, redirect, url_for, request
from app import app
from werkzeug.urls import url_parse
from app import app


@app.route('/')
@app.route('/index')
def index():
    title = "Home"
    return render_template('index.html', title=title)

@app.route('login', methods=['GET', 'POST'])
def login():
    return render_template()