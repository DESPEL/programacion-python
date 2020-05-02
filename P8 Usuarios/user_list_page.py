import tkinter as tk
import tkinter.font  as tkFont
import config
from config import HEIGHT, WIDTH, FONT10
from db import data

from circular_button import CircularButton
from text_properties import TextProperties
from user_info import UserInfoFrame


class _NavBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.config(bg=config.COLOR)

        self.title = tk.Label(
            self,
            fg=config.BG, bg=config.COLOR,
            text="Alumnos",
            font=("Arial", 16))

        self.title.place(
            anchor=tk.NW,
            x=72, y=38-24
        )


class _BodyFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        self.config(bg=config.BG)
        self.add_userbtn()

        self.title_2 = tk.Label(
            self,
            fg=config.COLOR, bg=config.BG,
            text="Personas",
            font=("Arial", 14))

        self.title_2.place(
            anchor=tk.NW,
            x=18, y=14
        )

        self.user_list = tk.Frame(self, width=WIDTH, height=491, bg=config.BG)
        self.user_list.place(
            anchor=tk.NW,
            x=0, y=45
        )

    def update(self):
        for child in self.user_list.winfo_children():
            child.destroy()
        py = 0
        for user in data["users"]:
            card = UserInfoFrame(self.user_list, self.controller, py, user)
            card.place(
                anchor=tk.NW,
                x=0, y=py
            )
            py += 72

        self.add_userbtn()

    def add_userbtn(self):
        text = TextProperties(
            fill="white",
            text="+",
            anchor="c",
            font="Consolas 20"
        )

        self.add_user = CircularButton(
            self, 28,
            config.COLOR, config.COLOR,
            lambda: self.controller.show("create_user"),
            text)

        self.add_user.place(
            anchor=tk.NW,
            x=286, y=HEIGHT-56-81
        )


class _NoUsersFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        tk.Label(self, text="NO HAY ALUMNOS",
            font=tkFont.Font(family='Arial', size=30)).place(
            anchor=tk.CENTER,
            relx=0.5, rely=0.5
        )

        self.config(bg=config.BG)
        self.add_userbtn()

    def add_userbtn(self):
        text = TextProperties(
            fill="white",
            text="+",
            anchor="c",
            font="Consolas 20"
        )

        self.add_user = CircularButton(
            self, 28,
            config.COLOR, config.COLOR,
            lambda: self.controller.show("create_user"),
            text)

        self.add_user.place(
            anchor=tk.NW,
            x=286, y=HEIGHT-56-81
        )


class UserListFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        self.nav_bar = _NavBar(self)
        self.nav_bar.place(anchor=tk.NW, width=WIDTH, height=56)

        self.body = _BodyFrame(controller, self)
        self.body.place(
            anchor=tk.NW,
            width=WIDTH,
            height=HEIGHT-56,
            y=56
        )

        self.no_users = _NoUsersFrame(controller, self)
        self.no_users.place(
            anchor=tk.NW,
            width=WIDTH,
            height=HEIGHT-56,
            y=56
        )

    def update(self):
        if data["users"]:
            self.body.tkraise()
            self.body.update()
        else:
            self.no_users.tkraise()
