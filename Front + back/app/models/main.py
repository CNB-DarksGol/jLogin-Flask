from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Email
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(message="Por favor, digite uma senha válido!")])

class ForgetMeForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
	nome = StringField('Username', validators=[DataRequired()])
	email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	password = PasswordField('Password', [InputRequired(), EqualTo('confpassword', message='Passwords must match')])
	confpassword = PasswordField('Password', validators=[DataRequired()])

class UpdatePasswordForm(FlaskForm):
	email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	password = PasswordField('Password', [InputRequired(), EqualTo('confpassword', message='Passwords must match')])
	confpassword = PasswordField('Password', validators=[DataRequired()])