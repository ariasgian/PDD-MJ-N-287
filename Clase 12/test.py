# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:18:06 2021

@author: arias
"""
from flask import Flask, json
app = Flask(__name__)


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
    if path == 'people':
        return 'usted va un JSON de personas'
    elif path == 'company':
        return 'aca va un JSON de empresas'
    else:
        return 'UPSSS.... no puedo buscar lo que estas pidiendo :('


app.run(port=3030, host='0.0.0.0')
