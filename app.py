import json, jinja2, time, os, data, json
from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
     return render_template("index.html")


@app.route("/quiz",methods=["GET","POST"])
def quiz():
     return render_template("quiz.html")

@app.route("/generatedlist/<loc>/<pop>/<spec>",methods=["GET","POST"])
def retgen(loc,pop,spec):
     gen = startgen(loc,pop,spec)
     retgen = json.loads(gen)
     return retgen

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
