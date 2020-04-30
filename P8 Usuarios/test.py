import tkinter as tk

from circular_button import CircularButton
from text_properties import TextProperties


class UserProfile(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text="asdfasdfasdfa").pack()

        text = TextProperties(
            fill="white",
            text="+",
            anchor="c",
            font="Consolas 20"
        )

        def test(): print("asdfasdf")

        CircularButton(self, 50, "#009789", "#009789", command=test, text=text).pack()


class UserPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.profile = UserProfile(master=self)
        self.label = tk.Label(self, text="BELOW")
        self.label.place(anchor=tk.NW, relwidth=1, relheight=0.5)
        self.profile.place(anchor=tk.NW, relwidth=1, relheight=0.5)
        self.profile.tkraise()
        self.bind("<ButtonRelease-1>", self._on_release)
        self.index = 0

    def _on_release(self, event):
        if self.index == 0:
            self.label.tkraise()
            self.index = 1
        else:
            self.profile.tkraise()
            self.index = 0
        print("asdfasd")


if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(300, 300)
    page = UserPage(window, bg="red")
    page.place(anchor=tk.NW, relwidth=1, relheight=1)

    window.mainloop()
