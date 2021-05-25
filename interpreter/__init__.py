from flask import Blueprint
from flask_restful import Api

interpreter_bp = Blueprint("interpreter", __name__, url_prefix="/interpreter")
interpreter_api = Api(interpreter_bp)

from . import routes
