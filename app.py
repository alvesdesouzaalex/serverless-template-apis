from collections import namedtuple
from random import choice

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/public/*": {"origins": "*"}})


@app.route("/public/website/newsletter", methods=["GET"])
def get_random_quote():
    resp = dict()
    return {
        "statusCode": 200,
        "data": [],
        "totalElements": 0
    }
