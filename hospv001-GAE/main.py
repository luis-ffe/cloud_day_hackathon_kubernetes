
#MEGABOSSES@42Porto

import os, uuid, datetime, pytz

from flask import Flask, render_template, request, redirect, url_for
from google.cloud import vision, translate, storage, datastore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
