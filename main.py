# imports
from crypt import methods
from flask import Flask, render_template
import os
from flask_mysqldb import MySQL
from database import *


# app setup
app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ.get("Mysql_user")
app.config['MYSQL_PASSWORD'] = os.environ.get("Mysql_pass")
app.config['MYSQL_DB'] = 'expense_manager'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.urandom(24)


@app.route("/")
def Home():
    return render_template('Home.html')

@app.route("/login",methods=["GET","POST"])
def Login():
    return render_template("Login.html")

@app.route("/register",methods=["GET","POST"])
def Register():
    return render_template("Register.html")

app.run(debug=True, host="0.0.0.0")