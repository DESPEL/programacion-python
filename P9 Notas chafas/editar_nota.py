import tkinter as tk
from PIL import ImageTk
from PIL import Image

import db
import config
from config import WIDTH, HEIGHT, FONT10, BG, FONT_COLOR, FONT12


class _NavBar(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.data = {}
        self.config(bg=config.COLOR)

        self.title = tk.Entry(
            self,
            fg=config.FONT_COLOR, bg=config.COLOR,
            font=("Arial", 16)
        )
        self.title.place(
            anchor=tk.NW,
            x=50, y=38-24
        )
        self.title.delete(0, "end")
        self.title.insert(0, "Placeholder text")

        self.create_btn = tk.Button(
            self,
            background=config.COLOR,
            activebackground=config.COLOR,
            borderwidth=0,
            fg=config.FONT_COLOR,
            font=config.FONT12(),
            text="Crear",
            width=4, height=1,
            command=lambda: controller.show("notes_frame", no_update=True)
        )
        self.create_btn.place(
            anchor=tk.NW,
            x=WIDTH-50, y=12
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
            command=lambda: controller.show("notes_frame", no_update=True)
        )
        self.return_btn.place(
            anchor=tk.NW,
            x=18, y=8
        )

    def update(self, data):
        self.data = data
        self.title.delete(0, "end")
        self.title.insert(0, data["title"])

    def on_hide(self):
        self.data["title"] = self.title.get()


class NoteFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        self.data = {
            "folder": "none",
            "name": "Placeholder note",
            "text": "Lorem ipsum sit dolor amet...",
            "date": "12/12/1212"
        }
        tk.Frame.__init__(self, *args, **kwargs)
        self.nav_bar = _NavBar(controller, master=self)
        self.nav_bar.place(anchor=tk.NW, width=WIDTH, height=56)

        self.content = tk.Text(
            self,
            bg=BG,
            fg=FONT_COLOR,
            width=40
        )
        self.content.place(
            x=16, y=72
        )
        self.content.delete("0.0", tk.END)
        self.content.insert(tk.INSERT, "texto de prueba")

        self.config(bg=config.BG)

    def save(self):
        pass

    def update(self, data):
        print(db.data)
        self.data = data
        self.content.delete("0.0", tk.END)
        self.content.insert(tk.INSERT, data["content"])
        self.nav_bar.update(data)

    def on_hide(self):
        print("Hiding")
        self.data["content"] = self.content.get("0.0", tk.END)
        self.nav_bar.on_hide()
        db.save_data()
        print("Note saved")


if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(config.WIDTH, config.HEIGHT)
    test = NoteFrame(None, window)
    test.place(anchor=tk.NW, relwidth=1, relheight=1)
    test.on_hide()

    window.mainloop()
