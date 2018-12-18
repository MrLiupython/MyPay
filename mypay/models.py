# -*- coding: utf-8 -*-
from mypay.ext import db
from datetime import datetime, timedelta
class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(8), default='no_name')
    age = db.Column(db.Integer, default=0)
    iphone_numble = db.Column(db.String(16), default='')
    address =  db.Column(db.String(8), default='')

class Record(db.Model):
    __tablename__ = "record" 
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(hours=8))
    user_id = db.Column(db.Integer, nullable=False)
    pay_num = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(16), default='')
    pay_kind = db.Column(db.String(16), default='')
    
