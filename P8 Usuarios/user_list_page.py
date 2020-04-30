import tkinter as tk

import config
from config import HEIGHT, WIDTH


from circular_button import CircularButton
from text_properties import TextProperties


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
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.config(bg=config.BG)
        print("abc")
        self.add_userbtn()

    def _init_windows(self):
        pass

    def update(self):
        pass

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
            lambda: print("pressed owo"),
            text)         

        self.add_user.place(
            anchor=tk.NW,
            x=286, y=HEIGHT-56-81
        )


class UserListFrame(tk.Frame):
    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.nav_bar = _NavBar(self)
        self.nav_bar.place(anchor=tk.NW, width=WIDTH, height=56)

        self.body = _BodyFrame(self)
        self.body.place(
            anchor=tk.NW,
            width=WIDTH,
            height=HEIGHT-56,
            y=56
        )


if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(WIDTH, HEIGHT)
    window.resizable(False, False)

    user_page = UserListFrame(bg=config.BG)
    user_page.place(anchor=tk.NW, relwidth=1, relheight=1)

    window.mainloop()
