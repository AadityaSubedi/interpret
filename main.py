from flask import Flask,Blueprint
from interpreter import interpreter_bp
from flask_restful import Resource,Api  



app = Flask(__name__)
app.register_blueprint(interpreter_bp, url_prefix='/interprete')


if __name__ == "__main__":
    app.run()