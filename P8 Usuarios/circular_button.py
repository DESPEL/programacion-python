import tkinter as tk

from text_properties import TextProperties
from config import BG


class CircularButton(tk.Canvas):
    def __init__(
        self, master, radius, color, bg, command=None, text=None, **kwargs
    ):
        self.command = command
        tk.Canvas.__init__(
            self,
            master,
            width=2*radius,
            height=2*radius,
            bd=0,
            highlightthickness=0,
            bg=BG,
            **kwargs
        )
        self.create_oval(
            (0, 0, 2*radius-1, 2*radius-1),
            fill=bg,
            outline=color
        )

        if text is not None:
            self.create_text(radius, radius, **text)

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


if __name__ == "__main__":
    def test():
        print("button working")

    text = TextProperties(
        fill="white",
        text="+",
        anchor="c",
        font="Consolas 20"
    )

    window = tk.Tk()
    btn = CircularButton(
        window, 30, "#009789", "#009789", command=test, text=text)
    btn.pack()

    window.mainloop()
