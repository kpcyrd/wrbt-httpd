#!/usr/bin/env python
from flask import Flask, Response, request
from ConfigParser import ConfigParser
from subprocess import check_output
import json
app = Flask(__name__)

CONF = 'wrbt-httpd.conf'


@app.route('/api', methods=['POST'])
def api():
    if open_router or request.form['auth'] == auth:
        if request.form['method'] == 'authorize':
            name = request.form['name']
            response = check_output(['yrd', 'peer', 'auth', '--json', name])
        else:
            response = json.dumps({'error', 'unknown method'})
    else:
        response = json.dumps({'error': 'rejected'})

    response = Response(response, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/')
def index():
    text = '''
    "But I don't want to go among mad people," Alice remarked.
    "Oh, you can't help that," said the Cat: "we're all mad here. I'm mad. You're mad."
    "How do you know I'm mad?" said Alice.
    "You must be," said the Cat, "or you wouldn't have come here."
    '''
    return Response(text, mimetype='text/plain')


if __name__ == '__main__':
    config = ConfigParser()
    config.read(CONF)
    auth = config.get('wrbt', 'auth')
    open_router = config.getboolean('wrbt', 'open')

    app.debug = True
    app.run()
