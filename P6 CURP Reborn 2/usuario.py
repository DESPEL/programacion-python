import os
import csv
import json

from random import choice, randint

from lib import safe_input
from reader import abreviaciones


class Usuario:
    def __init__(
        self,
        nombre,
        apellido_p,
        apellido_m,
        sexo,
        nacimiento,
        entidad
    ):
        self.nombre = nombre
        self.apellidos = [apellido_p, apellido_m]
        self.sexo = sexo
        self.nacimiento = nacimiento
        self.entidad = entidad

    @staticmethod
    def create():
        nombre = input("Ingrese su nombre: ")
        apellido_p = input("Ingrese su apellido paterno: ")
        apellido_m = input("Ingrese su apellido materno:")
        sexo = input("Ingrese su sexo (H/M): ")
        mes_n = safe_input(
            lambda x: x > 1 and x <= 12,
            "Ingrese el número de su mes de nacimiento ej. 03: ",
            "Ingrese un número de mes válido",
            type_=int
        )
        dia_n = safe_input(
            lambda x: x > 1 and x <= 31,
            "Ingrese el número de su dia de nacimiento: ",
            "Ingrese un número de dia válido",
            type_=int
        )
        ano_n = safe_input(
            lambda x: x > 1890 and x <= 2021,
            "Ingrese el número de su año de nacimiento: ",
            "Ingrese un número de año válido",
            type_=int
        )
        fecha_nacimiento = [dia_n, mes_n, ano_n]
        entidad = input("Ingrese su entidad de nacimiento ej,Baja California:")
        return Usuario(
            nombre,
            apellido_p,
            apellido_m,
            sexo,
            [dia_n, mes_n, ano_n],
            entidad
        )

    def generate_curp(self):
        first_last_name_part = self._get_name_part()
        second_last_name_part = self.apellidos[1][0].upper()
        name_part = self.nombre[0].upper()
        sex_part = self.sexo
        state_code = abreviaciones[self.entidad.upper()]
        inner_const = self._get_name_inner_cons()
        year_number = self._get_year_number()
        last_digit = randint(0, 9)

        return (
            first_last_name_part
            + second_last_name_part
            + name_part
            + str(self.nacimiento[2])[-1:-3]
            + str(self.nacimiento[1])
            + str(self.nacimiento[0])
            + sex_part
            + state_code
            + inner_const
            + str(year_number)
            + str(last_digit)
        )

    def _get_year_number(self):
        if self.nacimiento[2] < 1999:
            return randint(0, 9)
        else:
            return choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def _get_name_part(self):
        vocales = "AEIOU"
        parte = self.apellidos[0][0].upper()
        for letra in self.apellidos[0]:
            if letra.upper() in vocales:
                parte += letra.upper()
                break
        return parte

    def _get_name_inner_cons(self):
        last_name_inner = (
            self._get_inner_cons(self.apellidos[0].upper())
            + self._get_inner_cons(self.apellidos[1].upper())
        )
        name_inner = self._get_inner_cons(self.nombre)
        return last_name_inner + name_inner

    def _get_inner_cons(self, text):
        vocales = "AEIOU"
        for letter in text[1:]:
            if letter not in vocales:
                return letter.upper()

    def save(self):
        data = {}
        with open("usuarios.json", "r") as f:
            try:
                data = json.load(f)
            except Exception:
                pass

        if "users" not in data.keys():
            data["users"] = []

        data["users"].append({
            "nombre": self.nombre,
            "apellido_paterno": self.apellidos[0],
            "apellido_materno": self.apellidos[1],
            "sexo": self.sexo,
            "nacimiento": {
                "dd": str(self.nacimiento[0]),
                "mm": str(self.nacimiento[1]),
                "yyyy": str(self.nacimiento[2])
            },
            "estado": self.entidad,
            "curp": self.generate_curp()
        })

        with open("usuarios.json", "w") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    while True:
        print("Bienvenido al sistema de CURPS")
        Usuario.create().save()

        if input("Ingrese 1 si quiere agregar otro usuario: ") != "1":
            break
