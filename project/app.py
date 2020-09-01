from cs50 import SQL
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html") #,rows=rows)

@app.route("/imaginarymenu", methods=["GET", "POST"])
def getmenu():
    return render_template("menu.html")
