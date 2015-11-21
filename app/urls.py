# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

from app.handler.start import hello_world
from app.handler.calculator import add

app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)

@app.route('/', methods=['GET'])
def hello_world_handler():
    data = ""
    return hello_world(data)

@app.route('/calculator/add/<int:a>/<int:b>', methods=["GET"])
def calculator_add(a, b):
    #a = request.args.get('a')
    #b = request.args.get('b')
    return add(a, b)
