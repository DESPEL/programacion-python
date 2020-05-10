import tkinter as tk
import tkinter.font as tkFont
import config
from config import HEIGHT, WIDTH, FONT10
from db import data
import db
from PIL import ImageTk
from PIL import Image
from circular_button import CircularButton
from text_properties import TextProperties
from user_info import NoteInfoFrame
from folder_widget import folder_widget

import time
import datetime


class _NavBar(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.config(bg=config.COLOR)

        self.title = tk.Label(
            self,
            fg=config.FONT_COLOR, bg=config.COLOR,
            text="Notas",
            font=("Arial", 16))

        self.title.place(
            anchor=tk.NW,
            x=72, y=38-24
        )

        self.return_btn = tk.Button(
            self,
            background=config.COLOR,
            activebackground=config.COLOR,
            borderwidth=0,
            fg=config.FONT_COLOR,
            font=config.FONT16(),
            text="←",
            width=2, height=1,
            command=lambda: controller.show("folder_list")
        )
        self.return_btn.place(
            anchor=tk.NW,
            x=18, y=8
        )

        self.edit_btn = tk.Button(
            self,
            bg=config.COLOR,
            borderwidth=0,
            fg=config.FONT_COLOR,
            text="Renombrar",
            font=("Arial", 12),
            command=self.RenameFolder)

        self.edit_btn.place(
                anchor=tk.NW,
                x=301-20, y=44-28
            )

    def RenameFolder(self):
        self.wigdet = folder_widget(None)
        self.wigdet.set_text(self.data["title"])
        self.wigdet.place(x=140, y=205)
        self.create_button = tk.Button(
            anchor=tk.CENTER,
            bg=config.BG,
            text="Renombrar",
            font=("Arial", 12),
            command=self.hide_widget
        )
        self.create_button.place(
            x=150, y=280
        )

    def hide_widget(self):
        new_title = self.wigdet.get_text()
        self.wigdet.place_forget()
        self.create_button.place_forget()
        self.data["title"] = new_title
        db.save_data()
        self.master.update(self.data)

    def _update(self, data):
        self.data = data
        self.title.config(text=self.data["title"])


class _BodyFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        self.config(bg=config.BG)
        self.add_userbtn()

        self.title_2 = tk.Label(
            self,
            fg=config.FONT_COLOR, bg=config.BG,
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

    def update(self, data):
        self.data = data
        for child in self.user_list.winfo_children():
            child.destroy()
        py = 0
        for idx, note in enumerate(self.data["notes"]):
            card = NoteInfoFrame(self.user_list, self.controller, py, idx, self.data["notes"])
            card.place(
                anchor=tk.NW,
                x=0, y=py
            )
            py += 72

        self.add_userbtn()

    def add_userbtn(self):
        def add_note():
            today_format = time.strftime("%m/%d/%Y %H:%M:%S")
            self.data["notes"].append({
                "title": "Ingresar titulo",
                "date": str(today_format),
                "content": "Ingrese el contenido de la nota"
            })
            self.controller.show("note_frame", self.data["notes"][-1])

        self.icon = ImageTk.PhotoImage(Image.open("add_note_icon.png").resize((30, 30)))
        self.add_user = tk.Button(
            self,
            image=self.icon,
            borderwidth=0,
            command=add_note,
            bg=config.BG
        )

        self.add_user.place(
            anchor=tk.NW,
            x=286, y=HEIGHT-56-81
        )


class _NoUsersFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        tk.Label(
            self,
            text="NO HAY NOTAS",
            font=tkFont.Font(family='Arial', size=26)
        ).place(
            anchor=tk.CENTER,
            relx=0.5, rely=0.5
        )

        self.config(bg=config.BG)
        self.add_userbtn()

    def add_userbtn(self):
        def add_note():
            today_format = time.strftime("%m/%d/%Y %H:%M:%S")
            self.data["notes"].append({
                "title": "Ingresar titulo",
                "date": str(today_format),
                "content": "Ingrese el contenido de la nota"
            })
            self.controller.show("note_frame", self.data["notes"][-1])

        self.icon = ImageTk.PhotoImage(Image.open("add_note_icon.png").resize((30, 30)))
        self.add_user = tk.Button(
            self,
            image=self.icon,
            borderwidth=0,
            command=add_note,
            bg=config.BG
        )

        self.add_user.place(
            anchor=tk.NW,
            x=286, y=HEIGHT-56-81
        )

    def update(self, data):
        self.data = data
        self.add_userbtn()


class NotesFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.controller = controller

        self.nav_bar = _NavBar(controller, self)
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

    def update(self, data=None, no_update=False):
        if not no_update:
            self.data = data
            self.nav_bar._update(data)
        print("update")
        print(self.data)
        if self.data["notes"]:
            self.body.tkraise()
            self.body.update(self.data)
        else:
            self.no_users.tkraise()
            self.no_users.update(self.data)


if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(config.WIDTH, config.HEIGHT)
    test = NotesFrame(None, window)
    test.place(anchor=tk.NW, relwidth=1, relheight=1)

    window.mainloop()
