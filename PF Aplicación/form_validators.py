from wtforms import (
    ValidationError
)
from wtforms.validators import (
    StopValidation
)

import db

class UserExists(object):
    def __init__(self, message=None):
        self.message = message or "El usuario no existe"

    def __call__(self, form, field):
        if db.can_register(field.data):
            raise StopValidation(self.message)

class ValidatePassword(object):
    def __init__(self, message=None):
        self.message = message or "Contraseña incorrecta"

    def __call__(self, form, field):
        username = form.username.data
        if not db.login(username, field.data):
            raise StopValidation(self.message)

class CanRegister(object):
    def __init__(self, message=None):
        self.message = message or "Ya existe un usuario con ese nombre"

    def __call__(self, form, field):
        if not db.can_register(field.data):
            raise StopValidation(self.message)