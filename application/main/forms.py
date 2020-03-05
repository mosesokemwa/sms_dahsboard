from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional

from flask_wtf import FlaskForm
class RegistrationForm(FlaskForm):
    """User Signup Form."""

    name = StringField('Name',
                       validators=[DataRequired(
                           message=('Enter a fake name or something.'))])
    email = StringField('Email',
                        validators=[
                            Length(min=6, message=(
                                'Please enter a valid email address.')),
                            Email(message=('Please enter a valid email address.')),
                            DataRequired(message=('Please enter a valid email address.'))])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(
                                     message='Please enter a password.'),
                                 Length(min=6, message=(
                                     'Please select a stronger password.')),
                                 EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Your Password',)
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[
                             DataRequired('Uhh, your password tho?')])
    submit = SubmitField('Log In')


class MessageForm(FlaskForm):
    """Message Creation Form"""
    text_message = StringField('Text Message', validators=[
        Length(max=140, message=(
            'Please enter a text message  with 140 characters')),
        DataRequired('Please enter a text message .')])
    email = StringField('Email', validators=[
        Length(min=6, message=(
            'Please enter a valid email address.')),
        Email(message=('Please enter a valid email address.')),
        DataRequired(message=('Please enter a valid email address.'))])
    submit = SubmitField('Create Message')
