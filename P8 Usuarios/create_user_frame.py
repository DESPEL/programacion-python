import tkinter as tk

import config
import db
from config import HEIGHT, WIDTH
from text_properties import TextProperties
from text_input import TextInput, BigTextInput


class _NavBar(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.config(bg=config.COLOR)

        self.title = tk.Label(
            self,
            fg=config.BG, bg=config.COLOR,
            text="Agregar",
            font=("Arial", 16)
        )
        self.title.place(
            anchor=tk.NW,
            x=72, y=38-24
        )

        self.return_btn = tk.Button(
            self,
            background=config.COLOR,
            activebackground=config.COLOR,
            borderwidth=0,
            font=config.FONT16(),
            text="←",
            width=2, height=1,
            command=lambda: controller.show("user_list")
        )
        self.return_btn.place(
            anchor=tk.NW,
            x=19, y=38-24-6
        )


class _BodyFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        self.config(bg=config.BG)
        self._init_input()

        self.save_btn = tk.Button(
            self,
            background=config.COLOR,
            activebackground=config.COLOR,
            borderwidth=0,
            font=config.FONT12(),
            fg=config.BG,
            text="Agregar",
            width=10, height=2,
            command=lambda: self.save()
        )

        self.name_Lbl = tk.Label(
            self,
            fg=config.COLOR, bg=config.BG,
            text="Nombre",
            font=("Arial", 14)
        )

        self.name_Lbl.place(
            anchor=tk.NW,
            x=18, y=14
        )

        self.b_day_Lbl = tk.Label(
            self,
            fg=config.COLOR, bg=config.BG,
            text="Fecha de Nacimiento",
            font=("Arial", 14)
        )

        self.b_day_Lbl.place(
            anchor=tk.NW,
            x=18, y=207
        )

        self.desc_Lbl = tk.Label(
            self,
            fg=config.COLOR, bg=config.BG,
            text="Descripcion",
            font=("Arial", 14)
        )

        self.desc_Lbl.place(
            anchor=tk.NW,
            x=18, y=314
        )

        self.save_btn.place(
            anchor=tk.NW,
            x=135, y=494
        )

    def _init_input(self):
        normal_input = {
            "master": self,
            "width": 328, "height": 30
        }

        small_input = {
            "master":  self,
            "width": 74, "height": 30
        }
        big_input = {
            "master": self,
            "width": 328, "height": 74
        }
        input_list = {
            "name": {
                "text": "Nombre",
                "config": normal_input,
                "pos": {"x": 16, "y": 54}
            },
            "last_name_1": {
                "text": "Apellido Paterno",
                "config": normal_input,
                "pos": {"x": 16, "y": 104}
            },
            "last_name_2": {
                "text": "Apellido Materno",
                "config": normal_input,
                "pos": {"x": 16, "y": 234-80}
            },
            "b_day": {
                "text": "Día(01)",
                "config": small_input,
                "pos": {"x": 16, "y": 252}
            },
            "b_month": {
                "text": "Mes(01)",
                "config": small_input,
                "pos": {"x": 113, "y": 252}
            },
            "b_year": {
                "text": "Año(1994)",
                "config": small_input,
                "pos": {"x": 210, "y": 252}
            },
        }

        self.inputs = {}
        for tag, props in input_list.items():
            self.inputs[tag] = self.create_input(**props)

        self.inputs["desc"] = BigTextInput(**big_input)
        self.inputs["desc"].place(
            anchor=tk.NW,
            x=16, y=340
        )
        self.inputs["desc"].set_text("Lorem ipsum...")

    def create_input(self, text, config, pos):
        input_ = TextInput(
            **config,
        )
        input_.set_text(text)
        input_.place(
            anchor=tk.NW,
            **pos
        )
        return input_

    def clear(self):
        self.inputs["name"].set_text("Nombre"),
        self.inputs["last_name_1"].set_text("Apellido Paterno"),
        self.inputs["last_name_2"].set_text("Apellido Materno"),
        self.inputs["b_day"].set_text("Día(01)"),
        self.inputs["b_month"].set_text("Mes(01)"),
        self.inputs["b_year"].set_text("Año(1994)"),
        self.inputs["desc"].set_text("Lorem Ipsum..."),

    def save(self):
        db.add_user({
            "name": self.inputs["name"].get_text(),
            "last_name_1": self.inputs["last_name_1"].get_text(),
            "last_name_2": self.inputs["last_name_2"].get_text(),
            "b_day": self.inputs["b_day"].get_text(),
            "b_month": self.inputs["b_month"].get_text(),
            "b_year": self.inputs["b_year"].get_text(),
            "desc": self.inputs["desc"].get_text(),
        })
        self.controller.show("user_list")


class CreateUserFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller

        tk.Frame.__init__(self, *args, **kwargs)
        self.nav_bar = _NavBar(self.controller, self)
        self.nav_bar.place(anchor=tk.NW, width=WIDTH, height=56)

        self.body = _BodyFrame(controller, self)
        self.body.place(
            anchor=tk.NW,
            width=WIDTH,
            height=HEIGHT-56,
            y=56
        )

    def clear(self):
        self.body.clear()

    def update(self):
        self.clear()
