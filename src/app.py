from flask import Flask, make_response, jsonify,request
# from bd import Carros

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ("Help me please")

@app.get('/hello')
def say_hello():
    return {"message":"Help me please"}
  

app.run()