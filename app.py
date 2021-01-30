import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy

# Flask Setup
app = Flask(__name__)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') 

# Remove tracking modifications
 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


 