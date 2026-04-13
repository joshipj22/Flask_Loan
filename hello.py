from flask import Flask

# app is your master variable
app = Flask(__name__) # hello.py, 

# let's create endpoints.
@app.route("/") # '/' is the home page
def home():
    return "Hello, World!" 


@app.route("/ping")
def ping():
    return {'message': 'Pong to your Ping'}