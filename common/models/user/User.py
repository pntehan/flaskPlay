# coding: utf-8
from application import db

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	pwd = db.Column(db.String(255))
	name = db.Column(db.String(255))
	type = db.Column(db.Integer)

	def __init__(self, name, pwd, type):
		self.name = name
		self.pwd = pwd
		self.type = type