from app import db

class Registro(db.Model):
	__tablename__ = 'usuarios'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	nome = db.Column(db.String)

	def __init__(self, email, password, nome):
		self.email = email
		self.password = password
		self.nome = nome

	def __repr__(self):
		return '<Email %r>' % self.email
