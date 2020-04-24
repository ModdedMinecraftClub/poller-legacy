from base64 import b64encode

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return render_template("main.html", last={})


@app.route("/", methods=["POST"])
def post():
    with open("test.png", "rb") as f:
        data = f.read()
    img = b64encode(data).decode("utf-8")
    return render_template("main.html", img=img, last=request.form)
