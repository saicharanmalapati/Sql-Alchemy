from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)
db.create_all()


class User(db.Model):
    __tablename__ = 'example1'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)
    email = db.Column('email', db.String)

    def __repr__(self):
        return '<User {}>'.format(self.data)
