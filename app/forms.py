from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SnacksForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    kind = StringField('Kind', validators=[DataRequired()])
    submit = SubmitField('Add')
