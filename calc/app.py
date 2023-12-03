# Put your app in here.
from flask import Flask, request

app = Flask('__name__')

from operations import *

math_options = { 'add' : add, 'sub' : sub, 'mult' : mult, 'div' : div}

# def call_func(x, y, func):
#     try:
#         return dispatcher[func](x, y)
#     except:
#         return "Invalid function"

@app.route('/<math>')
def do_math(math):
    a = request.args['a']
    b = request.args['b']
    num1 = int(a)
    num2= int(b)
    do_math = math_options[math](num1,num2)
    mathing = str(do_math)
    return mathing
    
@app.route('/math/<math>')
def do_math_alternative(math):
    a = request.args['a']
    b = request.args['b']
    num1 = int(a)
    num2= int(b)
    do_math = math_options[math](num1,num2)
    mathing = str(do_math)
    return mathing
    
    
# @app.route('/<math>')
# def do_math(math):
#     term = request.args.getlist('term')
#     try:
#         num1 = int(term[0])
#         num2= int(term[1])
#     except:
#         return "Invalid number"
#     try:
#         do_math = math_options[math](num1,num2)
#         mathing = str(do_math)
#         return mathing
#     except:
#         return "Invalid function"
    