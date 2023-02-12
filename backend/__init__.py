from flask import Flask, render_template

PATH_templates='../frontend/templates'

def create_app():
    # create and configure the app
    app = Flask(__name__, template_folder=PATH_templates, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Linking! Hello, World!'

    # test frontend html
    @app.route("/login")
    def login():
        return render_template("login.html")

    return app
