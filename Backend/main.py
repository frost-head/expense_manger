# imports
from flask import Flask, json
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

# routes
@app.route('/')
def home():
    data = fetchone(mysql,"select * from Users")
    print(data)
    return f"<h1>Added DataBase Functionality</h1> <br> <p>Here it is running :</p>{data['name']}"



app.run(debug=True, host="0.0.0.0")