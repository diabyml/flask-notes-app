from . import db
from flask_sqlalchemy import sqlalchemy

# User:  id username pwd_hash    --> sqlalchemy auto-generated:  notes
# Note: id title description user_id --> sqlalchemy auto-generated: user
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    hash = db.Column(db.String(100))
    notes = db.relationship('Note',backref='user',lazy='dynamic')

    def __repr__(self):
        return f"User: {self.id} {self.username} {self.hash}"

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    time_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=sqlalchemy.sql.func.now())

    def __repr__(self):
        return f"Note: {self.id} {self.title} {self.description}"


