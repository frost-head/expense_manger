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
    session['user'] = 4
    if 'user' in session:
        return redirect('/')
    if request.method == "POST":
        username = request.form['username']
        passcode = request.form['password']
        data = fetchone(mysql, "select uid, password from Users where username = '{}'".format(username))
        if data:
            if bcrypt.check_password_hash(data['password'],passcode):
                session['user'] = data['uid']
                return redirect('/dashboard')
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
        uid = fetchone(mysql, "select uid from Users where username = '{}'".format(username))
        session['user'] = uid
        return redirect('/')
    return render_template("Register.html")

@app.route("/logout")
def Logout():
    if 'user' in session:
        session.pop('user')
        return redirect('/')
    else:
        return redirect("/login")

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        userdata = fetchone(mysql, "select name from Users where uid = {}".format(session['user']))
        expensedata = fetchall(mysql, "select * from Expenses where uid = {}".format(session['user']))
        incomedata = fetchall(mysql, "select * from Income where uid = {}".format(session['user']))
        return render_template('Dashboard.html', userdata=userdata, expensedata=expensedata, incomedata=incomedata)
    else:
        return redirect('/login')

@app.route('/addincome', methods=['GET','POST'])
def Income():
    if 'user' in session:

        if request.method == "POST":
            title = request.form['title']
            amount = request.form['amount']
            cat = request.form['cat']
            insert(mysql, 'insert into Income(title, amount, category, uid) values("{}",{},"{}",{})'.format(title, amount, cat, session['user']))
            return redirect('/dashboard')
        return render_template('Income.html',)
    
    else:
        return redirect('/login')

@app.route('/addexpenditure', methods=['GET','POST'])
def Expenditure():
    if 'user' in session:

        if request.method == "POST":
            title = request.form['title']
            amount = request.form['amount']
            cat = request.form['cat']
            if request.form['a_l'] == "Assest":
                a_l = 0
            else:
                a_l = 1
            insert(mysql, 'insert into Expenses(title, amount, category, uid, a_l) values("{}",{},"{}",{},{})'.format(title, amount, cat, session['user'],a_l))
            return redirect('/dashboard')
        return render_template('Expenditure.html',)
    
    else:
        return redirect('/login')

app.run(debug=True, host="0.0.0.0")