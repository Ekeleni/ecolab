from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = 'postgre://loc.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Cloumn(db.Integer , primary_key=True)