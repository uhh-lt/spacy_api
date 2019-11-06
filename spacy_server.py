#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Benjamin Milde'

import flask
from flask import jsonify, request
from flask_cors import CORS

import json
import spacy
import os

base_path = os.getcwd()

app = flask.Flask(__name__)
app.secret_key = 'asdf'
app._static_folder = base_path
app._static_files_root_folder_path = base_path

CORS(app)

language = 'de'
port = 9000
debug = True

nlp = spacy.load(language)

@app.route('/process', methods=["POST"])
def process():
    text = str(request.form['text'])

    print("Got new request text:", text)

    output = []

    for token in nlp(text):
        output.append((token.text, token.pos_, token.lemma_, token.dep_))

    return jsonify(output)

if __name__ == '__main__':
    print(' * Starting app with base path:',base_path)
    app.debug = True
    app.run(threaded=True, port=port)
