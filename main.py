# imports
from crypt import methods
from flask import Flask, redirect, render_template, request, session
import os
from flask_mysqldb import MySQL
from database import *
from flask_bcrypt import Bcrypt


# app setup
app = Flask(__name__)
mysql = MySQL(app)
bcrypt = Bcrypt(app)


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
    if 'user' in session:
        return redirect('/')
    if request.method == "POST":
        username = request.form['username']
        passcode = request.form['password']
        data = fetchone(mysql, "select uid, password from Users where username = '{}'".format(username))
        if data:
            if bcrypt.check_password_hash(data['password'],passcode):
                session['user'] = data['uid']
                return redirect('/')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return render_template("Login.html")

@app.route("/register",methods=["GET","POST"])
def Register():
    if 'user' in session:
        return redirect('/')
    if request.method == "POST":
        username = request.form['username']
        data = fetchone(mysql, "select uid from Users where username = '{}'".format(username))
        if data:
            return "username taken"
        name = request.form['name']
        email = request.form['email']
        passcode = request.form['password']
        pw_hash = bcrypt.generate_password_hash(passcode).decode('utf-8')
        querry = 'insert into Users(username, name, email, password) values("{}","{}","{}","{}")'.format(username, name, email, pw_hash)
        print(querry)
        insert(mysql, querry)
        # uid = fetchone(mysql, "select uid from Users where username = '{}'".format(username))
        # session['user'] = uid
        return redirect('/')
    return render_template("Register.html")

@app.route("/logout")
def Logout():
    if 'user' in session:
        session.pop('user')
        return redirect('/')
    else:
        return redirect("/login")

app.run(debug=True, host="0.0.0.0")