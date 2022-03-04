# imports
from flask import Flask, json
import os
# from flask_mysqldb import MySQL
# from database import *


# app setup
app = Flask(__name__)
# mysql = MySQL(app)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = os.environ.get("Mysql_user")
# app.config['MYSQL_PASSWORD'] = os.environ.get("Mysql_pass")
# app.config['MYSQL_DB'] = 'expense_manager'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.urandom(24)


@app.route("/")
def Home():
    return "<h1>API functionality Removed</h1>"

app.run(debug=True, host="0.0.0.0")