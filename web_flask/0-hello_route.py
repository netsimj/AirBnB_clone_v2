#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return render-template ("10-hbnb_filters.py")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
