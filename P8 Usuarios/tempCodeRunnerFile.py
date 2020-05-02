import tkinter as tk

from config import BG, COLOR, BAD_COLOR


class TextInput(tk.Canvas):
    def __init__(self, master, width, height, *args, **kwargs):
        self.canvas = tk.Canvas(self, master, width, height, *args, **kwargs)
        self.canvas.config(bg=BG)
        self.canvas.create_line(
            (0, height, width, height),
            color=COLOR,
            thickness=5
        )


if __name__ == "__main__":
    window = tk.Tk()
    test = TextInput(window, 50, 30)
    test.pack()

    window.mainloop()
