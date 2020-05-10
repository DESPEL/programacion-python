import tkinter as tk

from config import BG, COLOR, BAD_COLOR, FONT_COLOR


class TextInput(tk.Canvas):
    def __init__(self, master, width, height, canvas_args={}, entry_args={}):
        self.width = width
        self.height = height
        self.bottom_line = None

        tk.Canvas.__init__(
            self,
            master,
            width=width,
            height=height,
            borderwidth=0,
            bg=BG, bd=0, relief='ridge', highlightthickness=0,
            **canvas_args)
        self.config(bg=BG)

        self.change_color(COLOR)

        self.input = tk.Entry(
            self,
            bg=BG,
            fg=FONT_COLOR,
            borderwidth=0,
            **entry_args
        )
        self.input.place(
            x=0, y=0,
            width=width, height=height-2
        )

    def get_text(self):
        return self.input.get()

    def set_text(self, text):
        self.input.delete(0, "end")
        self.input.insert(0, text)

    def change_color(self, color):
        if not self.bottom_line:
            self.bottom_line = self.create_line(
                (0, self.height-1, self.width, self.height-1),
                fill=COLOR,
                width=2
            )
        self.itemconfig(self.bottom_line, fill=color)


class BigTextInput(tk.Canvas):
    def __init__(self, master, width, height, canvas_args={}, entry_args={}):
        self.width = width
        self.height = height
        self.bottom_line = None

        tk.Canvas.__init__(
            self,
            master,
            width=width,
            height=height,
            borderwidth=0,
            bg=BG, bd=0, relief='ridge', highlightthickness=0,
            **canvas_args)
        self.config(bg=BG)

        self.change_color(COLOR)

        self.input = tk.Text(
            self,
            bg=BG,
            fg=FONT_COLOR,
            borderwidth=0,
            **entry_args
        )
        self.input.place(
            x=0, y=0,
            width=width, height=height-2
        )

    def get_text(self):
        return self.input.get("0.0", tk.END)

    def set_text(self, text):
        self.input.delete("0.0", tk.END)
        self.input.insert(tk.INSERT, text)

    def change_color(self, color):
        if not self.bottom_line:
            self.bottom_line = self.create_line(
                (0, self.height-1, self.width, self.height-1),
                fill=COLOR,
                width=2
            )
        self.itemconfig(self.bottom_line, fill=color)


if __name__ == "__main__":
    window = tk.Tk()
    test = TextInput(window, 100, 40)
    test.pack()
    test.change_color(BAD_COLOR)

    window.mainloop()
