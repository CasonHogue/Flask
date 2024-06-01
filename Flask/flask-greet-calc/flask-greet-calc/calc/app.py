# Put your app in here.

from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a + b)

@app.route("/sub")
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a - b)

@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a * b)

@app.route("/div")
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a / b)

@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation == "add":
        return str(a + b)
    elif operation == "sub":
        return str(a - b)
    elif operation == "mult":
        return str(a * b)
    elif operation == "div":
        return str(a / b)
    else:
        return "Invalid operation"