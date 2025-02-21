from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,StringField
from wtforms.validators import DataRequired,Length,EqualTo,Email


class Login(FlaskForm):
    email=EmailField('email',validators=[
        DataRequired(),
        Length(max=50),
        Email()
    ])

    password=PasswordField('password',validators=[
        DataRequired(),
        Length(max=50),
    ])


class Register(FlaskForm):

    username=StringField('username',validators=[
        DataRequired(),
        Length(max=50),
    ])

    email=EmailField('email',validators=[
        DataRequired(),
        Length(max=50),
        Email()
    ])

    password=PasswordField('password',validators=[
        DataRequired(),
        Length(max=50)
    ])

    confirm=PasswordField('confirm',validators=[
        DataRequired(),
        Length(max=50),
        EqualTo('password',message='Contraseñas deben coincidir')
    ])


class Objeto(FlaskForm):
    foto=StringField('foto',validators=[
        DataRequired(),
        Length(max=20)
    ])

    descripcion=StringField('descripcion',validators=[
        DataRequired(),
        Length(max=50)
    ])

    