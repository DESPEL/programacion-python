import tkinter as tk

from config import BG, COLOR, BAD_COLOR, FONT_COLOR, DISCORD


class folder_widget(tk.Canvas):
    def __init__(self, master, canvas_args={}, entry_args={}):

        self.bottom_line = None

        tk.Canvas.__init__(
            self,
            master,
            width=110,
            height=110,
            borderwidth=0,
            bg=DISCORD, bd=0, relief='ridge', highlightthickness=0,
            **canvas_args)
        self.config(bg=DISCORD)

        self.titulo = tk.Label(
            self,
            text="Escriba el titulo",
            font=("Arial", 10),
            fg=COLOR,
            bg=DISCORD
        )

        self.titulo.place(
            x=5, y=10
        )
        self.input = tk.Entry(
            self,
            bg=BG,
            fg=FONT_COLOR,
            borderwidth=0,
            **entry_args
        )

        self.change_color(COLOR)
        self.input.place(
            x=5, y=50,
            width=100, height=20
        )

    def get_text(self):
        return self.input.get()

    def set_text(self, text):
        self.input.delete(0, "end")
        self.input.insert(0, text)

    def change_color(self, color):
        if not self.bottom_line:
            self.bottom_line = self.create_line(
                (0, 70, 110, 70),
                fill=COLOR,
                width=2
            )
        self.itemconfig(self.bottom_line, fill=color)
