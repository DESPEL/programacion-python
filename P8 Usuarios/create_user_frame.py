import tkinter as tk

import config
from config import HEIGHT, WIDTH


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


class CreateUserFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
