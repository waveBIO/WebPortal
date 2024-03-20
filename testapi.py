from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response, as_json
from testsql import *

app = Flask(__name__)
FlaskJSON(app)
CORS(app)



@app.route('/get_RSTRU')
def get_time():
    return jsonify({"result" : json_data})


@app.route('/increment_value', methods=['POST'])
def increment_value():
    data = request.get_json(force=True)
    try:
        value = int(data['value'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(value=value + 1)


@app.route('/get_value', methods=['GET'])

def get_value():
    if request.method == 'GET':
        value = request.args.get('wert')


    return value


if __name__ == '__main__':
    app.run()

