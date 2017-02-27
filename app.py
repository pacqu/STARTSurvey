import json, jinja2, time, os, json
from data import startgen
from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
     return render_template("index.html")


@app.route("/quiz",methods=["GET","POST"])
def quiz():
     if request.method == "POST":
          loc = request.form['location']
          pop = request.form['pop']
          spec = request.form['spec']
          return render_template("postquiz.html",loc=loc,pop=pop,spec=spec)
     else:
          return render_template("quiz.html")

@app.route("/generatedlist/<loc>/<pop>/<spec>",methods=["GET","POST"])
def retgen(loc,pop,spec):
     gen = startgen(loc,pop,spec)
     retgen = json.dumps(gen)
     #print retgen
     return retgen

if __name__ == '__main__':
     #retgen('rural','large','med')
     app.debug = True
     app.run(host='localhost',port=5000)
