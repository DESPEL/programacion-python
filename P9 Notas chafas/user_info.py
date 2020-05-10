import tkinter as tk
from PIL import ImageTk
from PIL import Image

from text_properties import TextProperties
from config import FONT16, FONT12, BG, FONT_COLOR, BAD_COLOR, WIDTH
from circular_button import CircularButton
import db


class FolderInfoFrame(tk.Frame):
    def __init__(self, master, controller, py, idx, data, *args, **kwargs):
        tk.Frame.__init__(self, master, width=360, height=72, *args, *kwargs)
        self.icon = ImageTk.PhotoImage(Image.open("folder_icon.png").resize((44, 48)))
        self.data = data
        self.dummy = tk.Label(master, image=self.icon).place(
            anchor=tk.NW,
            x=16, y=12+py
        )

        self.controller = controller

        abc = tk.Label(
            master,
            text=data.get("title"),
            font=FONT16(),
            bg=BG,
            fg=FONT_COLOR
        )
        abc.place(
            anchor=tk.NW,
            x=81, y=20+py
        )

        def delete_folder():
            del db.data["note"][idx]
            db.save_data()
            controller.show("folder_list")

        text = TextProperties(
            fill="white",
            text="x",
            anchor="c",
            font="Consolas 20"
        )
        self.delete = CircularButton(
            self, 22, BAD_COLOR, BAD_COLOR, delete_folder, text
        )
        self.delete.place(
            anchor=tk.NW,
            x=WIDTH-48, y=12
        )

        self.config(bg=BG)

        abc.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_release(self, e):
        self.controller.show("notes_frame", self.data)


class NoteInfoFrame(tk.Frame):
    def __init__(self, master, controller, py, idx, data, *args, **kwargs):
        tk.Frame.__init__(self, master, width=360, height=72, *args, *kwargs)
        self.data = data[idx]
        self.controller = controller

        abc = tk.Label(
            master,
            text=f"{self.data['title']}",
            font=FONT16(),
            bg=BG,
            fg=FONT_COLOR
        )
        abc.place(
            anchor=tk.NW,
            x=81, y=16+py
        )
        lbl = tk.Label(
            master,
            text=f"{self.data['date']}",
            font=FONT12(),
            bg=BG,
            fg=FONT_COLOR
        )
        lbl.place(
            anchor=tk.NW,
            x=81, y=38+py
        )
        self.config(bg=BG)

        def delete_note():
            print(type(data))
            del data[idx]
            db.save_data()
            self.controller.show("notes_frame", no_update=True)

        text = TextProperties(
            fill="white",
            text="x",
            anchor="c",
            font="Consolas 20"
        )
        self.delete = CircularButton(
            self, 22, BAD_COLOR, BAD_COLOR, delete_note, text
        )
        self.delete.place(
            anchor=tk.NW,
            x=WIDTH-48, y=12
        )

        lbl.bind("<ButtonRelease-1>", self._on_release)
        abc.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_release(self, e):
        self.controller.show("note_frame", self.data)


if __name__ == "__main__":
    window = tk.Tk()
    UserInfoFrame(window, None, 0, {
        "name": "asdfasd",
        "b_day": "12",
        "b_month": "21",
        "b_year": "2312"
    }).pack()
