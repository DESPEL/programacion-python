import tkinter as tk
from PIL import ImageTk
from PIL import Image

import config
from config import WIDTH, HEIGHT, FONT10, BG, FONT_COLOR, FONT12


class _NavBar(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.config(bg=config.COLOR)

        self.title = tk.Label(
            self,
            fg=config.BG, bg=config.COLOR,
            text="Perfil",
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


class ProfileFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.nav_bar = _NavBar(controller, self)
        self.nav_bar.place(anchor=tk.NW, width=WIDTH, height=56)
        self.icon = ImageTk.PhotoImage(Image.open("icon.png").resize((64, 68)))

        self.config(bg=config.BG)

        dy = 100

        self.Photo = tk.Label(self, image=self.icon).place(
            anchor=tk.NW,
            x=16, y=24+dy
        )
        self.name = tk.Label(
            self,
            text=f"",
            font=FONT12(),
            bg=BG,
            fg=config.COLOR
        )

        self.name.place(
            anchor=tk.NW,
            x=85, y=45+dy
        )
        self.b_day = tk.Label(
            self,
            text="",
            font=FONT10(),
            bg=BG,
            fg=FONT_COLOR
        )

        self.b_day.place(
            anchor=tk.NW,
            x=85, y=70+dy
        )

        self.DescTit = tk.Label(
            self,
            text="Descripcion",
            font=FONT12(),
            bg=BG,
            fg=config.COLOR
        )

        self.DescTit.place(
            anchor=tk.NW,
            x=18, y=170+dy
        )

        self.Desc = tk.Message(
            self,
            text="",
            font=FONT12(),
            bg=BG,
            fg=FONT_COLOR,
            width=300
        )

        self.Desc.place(
            anchor=tk.NW,
            x=18, y=190+dy
        )

    def update(self, data):
        self.Desc.config(text=data['desc'])
        self.b_day.config(text=f"{data['b_day']} {data['b_month']} {data['b_year']}")
        self.name.config(text=f"{data['name']} {data['last_name_1']} {data['last_name_2']}")
        print(data)
