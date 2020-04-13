from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    title = "Home"
    return render_template('index.html', title=title)
