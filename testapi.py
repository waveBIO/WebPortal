from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response, as_json
from testsql import *

app = Flask(__name__)
FlaskJSON(app)
CORS(app)

testusern = 'test'
testpassw = 'test'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        # db vergleich login data
        if username == testusern and password == testpassw:
        # Bei erfolgreicher Anmeldung weiterleiten
            return redirect(url_for('load_index'))
            #return 'Login erfolgreich.'
        else:
            return 'Falsche Benutzerdaten. Bitte versuchen Sie es erneut.'
    return render_template('login.html')

@app.route('/get_KREDSTRU')
def get_kredstru():
    return jsonify({"result" : json_data1})

@app.route('/get_ROHKREDSTRU')
def get_rohkredstru():
    return jsonify({"result" : json_data2})

@app.route('/index')
def load_index():
    return render_template('index.html')
    #return 'hat geklappt'

@app.route('/app.js')
def load_appjs():
    return render_template('app.js')
    #return 'hat geklappt'

    
# @app.route('/increment_value', methods=['POST'])
# def increment_value():
#     data = request.get_json(force=True)
#     try:
#         value = int(data['value'])
#     except (KeyError, TypeError, ValueError):
#         raise JsonError(description='Invalid value.')
#     return json_response(value=value + 1)


# @app.route('/get_value', methods=['GET'])

# def get_value():
#     if request.method == 'GET':
#         value = request.args.get('wert')


#    return value


if __name__ == '__main__':
    app.run(debug=True)

