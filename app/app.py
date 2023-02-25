#! /usr/bin/python
from flask import Flask, render_template, request
import base64
import pickle
import bleach
#import yaml

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    try:
        data = base64.urlsafe_b64decode(request.form['text'])
        data = bleach.clean(data)
        output = pickle.load(data)
    except Exception as e:
        output = e
    return render_template('home.html', code=output)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
