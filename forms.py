from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class ParamsForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	submit = SubmitField('Register')

