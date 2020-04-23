import tkinter as tk

from font import get_win_font


def get_style():
    return {
        "label": {
            "bg": "#3b7588",
            "fg": "white",
            "font": get_win_font
        }
    }


def get_frame_settings():
    return {
        "anchor": tk.NW,
        "relwidth": 1,
        "relheight": 0.2
    }


class Result:
    def __init__(self, master):
        self.master = master

        self._create_frame()
        self._place_label()

    def _create_frame(self):
        self.frame = tk.Frame(self.master)
        self.frame.place(**get_frame_settings())

    def _place_label(self):
        self.label = tk.Label(self.frame, **get_style()["label"])
        self.label.place(anchor=tk.NW, relwidth=1, relheight=1)
