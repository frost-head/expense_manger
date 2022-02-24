# imports
from flask import Flask

# app setup
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return "<h1>Flask Setup Complete</h1>"



app.run(debug=True, host="0.0.0.0")