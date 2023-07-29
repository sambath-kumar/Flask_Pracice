from flask import Flask, request
import json

# create flask application
sam = Flask(__name__)  # call entry point
# app is a object, it may any name
# sam is aobject name instead app
@sam.route('/')   # route() assign various url
def home():
    return "welcome to home page!"  

@sam.route('/calc', methods=["GET"]) 
def math_op():   # math_op is a method
    op = request.json["op"]   # requesting from postman (json)
    n1 = request.json["n1"]
    n2 = request.json["n2"]
    if op == "add":
        res = int(n1)+int(n2)
    elif op == "sub":
        res = int(n1)-int(n2)
    elif op == "mul":
        res = int(n1)*int(n2)
    else:
        res = int(n1)/int(n2)
    return "the {} result is {}".format(op,res)    
print(__name__)

if __name__ == "__main__":
    sam.run(debug = True) 