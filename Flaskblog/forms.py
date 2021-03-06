from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from Flaskblog.models import User
from flask_login import current_user


class RegestrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'This username is already exist! Please choose a different one.')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'This email is already exist! Please choose a different one.')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class AccountUpdateForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    picture = FileField('Update Porfile Picture',
                        validators=[FileAllowed(['png', 'jpg'])])

    submit = SubmitField('Update')

    def validate_username(self, username):

        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'This username is already taken! Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'This email is already taken! Please choose a different one.')


class PostForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])

    content = TextAreaField('Content', validators=[DataRequired()])

    submit = SubmitField('Post')
