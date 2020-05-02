import tkinter as tk
from PIL import ImageTk
from PIL import Image

from config import FONT16, FONT12, BG, FONT_COLOR


class UserInfoFrame(tk.Frame):
    def __init__(self, master, controller, py, data, *args, **kwargs):
        tk.Frame.__init__(self, master, width=360, height=72, *args, *kwargs)
        self.icon = ImageTk.PhotoImage(Image.open("icon.png").resize((44, 48)))
        self.data = data
        self.dummy = tk.Label(master, image=self.icon).place(
            anchor=tk.NW,
            x=16, y=12+py
        )

        self.controller = controller

        abc = tk.Label(
            master,
            text=f"{data['name']} {data['last_name_1']} {data['last_name_2']}",
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
            text=f"{data['b_day']}, {data['b_month']}, {data['b_year']}",
            font=FONT12(),
            bg=BG,
            fg=FONT_COLOR
        )
        lbl.place(
            anchor=tk.NW,
            x=81, y=38+py
        )
        self.config(bg=BG)

        lbl.bind("<ButtonRelease-1>", self._on_release)
        abc.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_release(self, e):
        self.controller.show("profile_frame", self.data)


if __name__ == "__main__":
    window = tk.Tk()
    UserInfoFrame(window, None, {
        "name": "asdfasd",
        "b_day": "12",
        "b_month": "21",
        "b_year": "2312"
    }).pack()

    window.mainloop()
