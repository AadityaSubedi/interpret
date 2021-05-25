from flask_restful import Resource
from . import interpreter_api
from flask import Flask, request
import os
import subprocess


@interpreter_api.resource("")
class Intrepreter(Resource):
    def get(self):
        data = request.get_json()
        print(data)
        # return data
        # create temporary.py file
        filepath = "database/tmp.txt"
        with open(filepath, "w") as f:
            f.write(data["code"])

        # run the file on the shells
        a = subprocess.check_output(
            ["python", filepath, *data["arguments"]]).decode("utf-8")

        # return the command line output as the reesponse
        return {
            "output": a
        }
