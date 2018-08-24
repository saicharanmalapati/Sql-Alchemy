from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey(
                    'tag.id'), primary_key=True),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True))


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship(
        'Tag', secondary=tags, lazy='subquery', backref=db.backref('pages', lazy=True))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
