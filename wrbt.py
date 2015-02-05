#!/usr/bin/env python
from flask import Flask, Response, request, jsonify
from ConfigParser import ConfigParser
from subprocess import check_output
import hmac
import json
app = Flask(__name__)

CONF = 'wrbt-httpd.conf'


@app.route('/api', methods=['POST'])
def api():
    payload = request.form['payload']

    if 'auth' in request.form:
        token = request.form['auth'].encode('ascii')
        signed = hmac.new(auth, payload).hexdigest()
        authorized = hmac.compare_digest(token, signed)
    else:
        authorized = False

    if open_router or authorized:
        if request.form['method'] == 'authorize':
            name = request.form['name']
            response = check_output(['yrd', 'wrbt', 'confirm', '--', name, payload]).strip()
            response = {'response': response}
        else:
            response = {'error', 'unknown method'}
    else:
        response = {'error': 'rejected'}

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Request-Method', 'POST')
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
