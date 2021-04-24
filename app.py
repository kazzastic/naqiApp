from flask import Flask, request, Response, url_for
from flask import render_template
import numpy as np
import os
from os.path import dirname, abspath

ParentFolder = os.path.dirname(__file__)
app = Flask(__name__)


@app.route('/')
def hello(name=None):
    images = []
    folder = ParentFolder + '/static'
    for filename in os.listdir(folder):
        images.append(filename)

    return render_template('slider.html', len=len(images), images=images)


if __name__ == '__main__':
    app.run(debug=True)