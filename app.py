import os
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return {"status": "OK"}

@app.route("/students")
def students():
    return jsonify([
        {
            "id": "2MM20ND",
            "name": "Leo DiCaprio",
            "email": "dicaprio@gmail.com"
        },
        {
            "id": "9MM19ND",
            "name": "Berik Serik",
            "email": "berik@gmail.com"
        }
    ])

@app.route("/about")
def about():
    return {
        "organization": "KBTU",
        "phone": "+7077077070",
        "desc": "Top IT university"
    }

@app.route("/profile")
def profile():
    return {
        "id": "1",
        "name": "Berik",
        "surname": "Serik",
        "photo": "No"
    }    

@app.route("/version")
def version():
    return {
        "version": "v1.0.1"
    }  

@app.route("/student/<name>")
def student(name):
    return 'Student name is ' + name.capitalize()       

@app.route("/")
def hello():
    return 'Hello from ' + os.environ['HOSTNAME']    

if __name__=="__main__":
    app.run(host='0.0.0.0', port='9000')

