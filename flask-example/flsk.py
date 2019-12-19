from flask import Flask, escape, request
# https://www.palletsprojects.com/p/flask/

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

'''
$ env FLASK_APP=flsk.py flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
'''