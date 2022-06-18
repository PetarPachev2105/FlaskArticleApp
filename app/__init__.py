from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder='../templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///articles.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)