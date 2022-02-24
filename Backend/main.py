# imports
from flask import Flask, json
import os
from flask_mysqldb import MySQL
from database import *
from flask_restful import Resource, Api, reqparse


# app setup
app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ.get("Mysql_user")
app.config['MYSQL_PASSWORD'] = os.environ.get("Mysql_pass")
app.config['MYSQL_DB'] = 'expense_manager'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.urandom(24)



user_parser = reqparse.RequestParser()
user_parser.add_argument('Name', type=str, help='Name of user')
user_parser.add_argument('Username', type=str, help='Username for user')
user_parser.add_argument('Password', type=str, help='Password for user')



# classes
class users(Resource):
    def post(self):
        args = user_parser.parse_args()
        print(args)
        insert(mysql,f"insert into Users(name, username, password) values('{args['Name']}', '{args['Username']}', '{args['Password']}')")
        return {'operation':"success"}
    
    def get(self):
        return fetchall(mysql, "select * from Users")


api.add_resource(users, '/createuser')

app.run(debug=True, host="0.0.0.0")