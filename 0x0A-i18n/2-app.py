#!/usr/bin/env python3
''' Basic Flas app with Babel'''
from flask import Flask, render_template
from flask_baberl import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''babel config class'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale():
    '''get locale funciont'''
    return request.acceptlenguajes.best_match(Config.LANGUAGES)


@app.route('/', methods=["GET"])
def index():
    return (render_template('2-index.html'))


if (__name__ == '__main__'):
    app.run(port=3000, debug=True)
