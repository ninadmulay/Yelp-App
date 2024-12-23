from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

yelp = Flask(__name__)
yelp.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/yelpdb'
yelp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(yelp)
CORS(yelp)