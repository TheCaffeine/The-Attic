import re
from flask_wtf import Form
from flask_babel import lazy_gettext

from wtforms.fields import TextField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import url, length, regexp, optional, Required, Email, Length, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    """
        Login form
    """
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """
        Registration form
    """
    name = StringField('Full Name', validators=[Required()])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[
                        Required(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Create Account')

    def validate_check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(
                'Email already registered. Please proceed to login!')

    def validate_check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(
                'Username already in use. Please use another username.')


class SettingsForm(Form):
    """docstring for SettingsForm"""

    ui_lang = SelectField(
        label=lazy_gettext("Primary site language"),
        description=lazy_gettext("Site will try to show UI labels using this " +
            "language. User data will be shown in original languages."),
    )
    url = URLField(
        label=lazy_gettext("Personal site URL"),
        description=lazy_gettext("If you have personal site and want to share " +
            "with other people, please fill this field"),
        validators=[optional(), url(message=lazy_gettext("Invalid URL."))])
    username = TextField(
        label=lazy_gettext("Public profile address"),
        description=lazy_gettext("Will be part of your public profile URL. Can " +
            "be from 2 up to 40 characters length, can start start from [a-z] " +
            "and contains only latin [0-9a-zA-Z] chars."),
        validators=[
            length(2, 40, message=lazy_gettext("Field must be between 2 and 40" +
            " characters long.")),
            regexp(r"[a-zA-Z]{1}[0-9a-zA-Z]*",
                re.IGNORECASE,
                message=lazy_gettext("Username should start from [a-z] and " +
                    "contains only latin [0-9a-zA-Z] chars"))
        ]
    )