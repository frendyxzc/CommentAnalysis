# coding: utf-8
from __future__ import unicode_literals
import sys;reload(sys);sys.setdefaultencoding('utf8')

import json
from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
	return 'hello'

@app.route("/get/<string:query>")
def get_raw_response(query):
	return str(query)
	

if __name__ == "__main__":
	app.run()
