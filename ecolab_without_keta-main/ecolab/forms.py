from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, Required

class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[Length(min=4, max=25), DataRequired()])
    email = StringField('Email Address:', validators=[Length(min=6, max=35), Email()])
    password = PasswordField('New Password:', validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    data = [username, email, password]

    def data_return(self):
        return self.data

class LoginForm(FlaskForm):
    username =  StringField('Login', validators=[Required()])
    password = PasswordField('Password', validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    remember_me = BooleanField('remember me', default = False)

