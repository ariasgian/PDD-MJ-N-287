#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:36:28 2021

@author: gian
"""
from flask import Flask, json
from pymongo import MongoClient
from urllib.parse import urlencode
import settings
from os import environ

USER = eviron["DB_USER"]
PASS = eviron["DB_PASS"]
HOST = eviron["DB_HOST"]
BASE = eviron["DB_NAME"]

app = Flask(__name__)

print("##### Inicio Variable de entorno ###")
print(environ)
print("##### Fin Variable de entorno ###")


#######  MongoDB   ######
params = {
    'retryWrites': 'true',
    'w': 'majority',
    'ssl': 'true',
    'ssl_cert_reqs': 'CERT_NONE'
}

client = MongoClient(
    "mongodb+srv://" + USER + ':' + PASS + '@' +HOST + '/' + BASE + "?+urlencode(params))
db = client

##########
# %%


@app.route('/')
def hello_flask():
    return '<h1>Hola Mundo</h1>'


@app.route('/users')
def twitterUsers():
    users = [
        {'name': 'smessina_'},
        {'name': 'eantech'},
        {'name': 'TinchoLutter'},
        {'name': 'bitcoinArg'}
    ]
    response = app.response_class(response=json.dumps(
        users), status=200, mimetype='application/json')
    return response


@app.route('/users/<path>')
def searchUser(path):
    data = db["PDD-MJ-N-287"]
    test = data["twitter"]
    users = test.find({'type': path}).limit(10)
    result = []

    for user in users:
        item = {
            'usuario': user['name']
        }
        result.append(item)
    response = app.response_class(response=json.dumps(
        result), status=200, mimetype='application/json')
    return response

    """if path == 'people':
        return 'usted va un JSON de personas'
    elif path == 'company':
        return 'aca va un JSON de empresas'
    else:
        return 'UPSSS.... no puedo buscar lo que estas pidiendo :('"""


@app.route('/test')
def test():
    data = db["PDD-MJ-N-287"]
    test = data["twitter"]

    users = test.find()
    for user in users:
        print(user['name'], user['type'])
    return "mira la consola...."


app.run(port=3030, host='0.0.0.0')
