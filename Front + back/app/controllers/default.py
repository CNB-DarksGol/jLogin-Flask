from flask import Flask,redirect
from flask import render_template
from flask_mail import Mail, Message
from app import app

from app import db
from app.models.tables import Registro
from app.models.main import LoginForm, CreateAccountForm, UpdatePasswordForm


# LOGIN

@app.route('/', methods=['GET','POST'])
def login():

	form = LoginForm()
	r = Registro.query.filter_by(email=f"{form.email.data}").first()

	if form.validate_on_submit():
		if form.email.data == r.email and form.password.data == r.password:
			return redirect('forgetme')

	return render_template('index.html', form=form) 

# PEDIR NOVA SENHA

@app.route('/forgetme', methods=['GET'])
def forgetme():
	return render_template('forgetme.html')

# CRIAR NOVA SENHA 

@app.route('/newpassword', methods=['GET', 'POST'])
def newpassword():
	form = UpdatePasswordForm()
	r = Registro.query.filter_by(email=f"{form.email.data}").first()

	if form.validate_on_submit():
		if form.password.data == form.confpassword.data:
			r.password = form.password.data
			r.confpassword = form.confpassword.data

			db.session.add(r)
			db.session.commit()

	return render_template('rec.html', form=form)

# CRIAR NOVA CONTA

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
	form = CreateAccountForm()

	if form.validate_on_submit():
		i = Registro(form.email.data, form.password.data, form.nome.data)
		db.session.add(i)
		db.session.commit()

	return render_template('create_account.html', form=form)

# PAGINA INICIAL

@app.route('/home', methods=['GET'])
def home():
	i = Registro('admin@admin.com', 'admin', 'Administrador')
	db.session.add(i)
	db.session.commit()

	return 'ok'