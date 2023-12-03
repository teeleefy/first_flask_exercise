from flask import Flask

app = Flask("__name__")

#In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:
# /welcome   Returns “welcome”
# /welcome/home   Returns “welcome home”
# /welcome/back   Return “welcome back”
# Once you’ve finished this, run the tests for it:
# $python3 -m unittest test.py

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():

    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():

    return "Welcome back"

