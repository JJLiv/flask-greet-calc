from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "WELCOME"

@app.route("/welcome/home")
def welcome_home():
    return "WELCOME HOME!!"

@app.route("/welcome/back")
def welcome_back():
    return "WELCOME BACK!"
