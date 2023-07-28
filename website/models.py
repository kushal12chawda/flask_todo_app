from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(150),unique=True)
    user_password = db.Column(db.String(150),unique=True)
    user_name = db.Column(db.String(150),unique=True)
    todo = db.relationship('Todo',backref='user')
    task = db.relationship('Task',backref='user')  #tasl

    def get_id(self):
        return (self.user_id)

class Todo(db.Model,UserMixin):
    todo_id = db.Column(db.Integer,primary_key=True)
    todo_name = db.Column(db.String(150),unique=True)
    todo_date = db.Column(db.DateTime,nullable=False,default=func.now()) 
    user_fk = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    task = db.relationship('Task',backref='todo')

class Task(db.Model,UserMixin):
    task_id = db.Column(db.Integer,primary_key=True)
    task_name = db.Column(db.String(150))
    task_desc = db.Column(db.Text)
    task_status = db.Column(db.Boolean,nullable=False,default=False)
    user_fk = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    todo_fk = db.Column(db.Integer,db.ForeignKey('todo.todo_id'))

    