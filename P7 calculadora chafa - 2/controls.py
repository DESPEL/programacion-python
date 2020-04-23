import tkinter as tk

import control_button


def get_frame_settings():
    return {
        "anchor": tk.NW,
        "relwidth": 1,
        "relheight": 0.8,
        "rely": 0.2,
    }


class Controls:
    def __init__(self, master, result_label):
        self.master = master
        self.result = result_label

        self._create_frame()
        self._create_buttons()

    def _create_frame(self):
        self.frame = tk.Frame(self.master)
        self.frame.place(**get_frame_settings())

    def _create_buttons(self):
        control_button.create_numpad(self.master, self.result)
        control_button.create_operation_btns(self.frame, self.result)
