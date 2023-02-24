from flask import Flask, render_template, request
from flask_cors import *

PATH_templates='../frontend/templates'

def create_app():
    # create and configure the app
    app = Flask(__name__, template_folder=PATH_templates, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    @cross_origin()
    def hello():
        return 'Linking! Hello, World!'

    # test frontend html
    @app.route("/login")
    @cross_origin()
    def login():
        return render_template("login.html")

    # test json
    @app.route("/welcome")
    @cross_origin()
    def welcome():
        return {
            "Class": "ISDN 4002",
            "Project": "Linking"
        }
    
    # test received data from uniapp
    @app.route("/request")
    @cross_origin()
    def get_text_input():
        text = request.args.get('inputstr')
        print(text)
        return text

    return app
