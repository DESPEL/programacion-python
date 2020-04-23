import tkinter as tk

import settings

from font import get_win_font
from button_templates import get_operation_buttons_settings

btn_settings = {
    "normal": {
        "anchor": tk.NW,
        "relwidth": 1/settings.CONTROL_COLUMNS,
        "relheight": 1/settings.CONTROL_ROWS
    },
    "double": {
        "anchor": tk.NW,
        "relwidth": 2/settings.CONTROL_COLUMNS,
        "relheight": 1/settings.CONTROL_ROWS
    }
}


def get_button_style():
    return {
        "bg": "#163f4d",
        "fg": "white",
        "font": get_win_font()
    }


def gen_callback(i, j, res_label):
    def callback():
        value = str((i*3)+(j+1))
        res_label.config(text=res_label.cget("text")+value)
    return callback


def place_button(button, row, column, x=0):
    type_ = "normal" if x != 1 else "double"
    button.place(
        **btn_settings[type_],
        relx=column/settings.CONTROL_COLUMNS,
        rely=row/settings.CONTROL_ROWS
    )


def create_button(master, text, command, row, column, x=0):
    button = tk.Button(
        master,
        command=command,
        text=text,
        **get_button_style()
    )
    place_button(button, row, column, x)


def create_numpad(master, res_label):
    for i in range(3):
        for j in range(3):
            create_button(
                master,
                str((i*3)+(j+1)),
                gen_callback(i, j, res_label),
                3-i, j
            )
    create_button(
        master,
        "0",
        gen_callback(0, -1, res_label),
        settings.CONTROL_ROWS-1, 0, 1
    )


def create_operation_btns(master, res_label):
    for button in get_operation_buttons_settings(res_label).values():
        create_button(master, **button)
