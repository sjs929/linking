'''
用于验证Flask框架是否安装成功
'''
from flask import Flask, url_for, redirect, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

@app.route("/login")
def login():
	return render_template("./frontend/templates/login.html")