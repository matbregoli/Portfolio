from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class addressForm(FlaskForm):
	address = StringField('Address', )

	submit = SubmitField('Enter Address')