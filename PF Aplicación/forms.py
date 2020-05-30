from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField, PasswordField,
    BooleanField, SubmitField
)
from wtforms.validators import (
    DataRequired, ValidationError,
    EqualTo,
    InputRequired
)

from form_validators import (
    UserExists,
    ValidatePassword,
    CanRegister
)

import db

class RegisterForm(FlaskForm):

    username = StringField(
        "Usuario",
        validators=[InputRequired(), CanRegister()]
    )

    password = PasswordField(
        "Contraseña", 
        validators=[InputRequired()],
    )

    password2 = PasswordField(
        "Confirmar contraseña",
        validators=[InputRequired(), EqualTo(
            'password', 
            message="Las contraseñas deben de ser iguales")]
    )

class LoginForm(FlaskForm):
    username = StringField(
        "Nombre de usuario", 
        validators=[InputRequired(), UserExists()]
    )

    password = PasswordField(
        "Contraseña",
        validators=[InputRequired(), ValidatePassword()]
    )