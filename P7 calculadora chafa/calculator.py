import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk

window = tk.Tk()

win_font = tkFont.Font(family="Arial", size="20")

last_num = ""
operations = {
    "sum": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mult": lambda x, y: x * y,
    "div": lambda x, y: x / y
}
operation = ""


def gen_operation_callback(op):
    def callback():
        global operation
        global last_num

        operation = op
        last_num = res_label.cget("text")
        res_label.config(text="")
    return callback


def change_sign_callback():
    num = float(res_label.cget("text"))
    num *= -1
    res_label.config(text=str(num))


def percent_callback():
    num = float(res_label.cget("text"))
    num /= 100
    res_label.config(text=str(num))


def AC_callback():
    global last_num
    global operation

    res_label.config(text="")
    last_num = ""
    operation = ""


def solve_callback():
    global operation
    global last_num

    if not operation or not last_num:
        return

    x = float(last_num)
    y = float(res_label.cget("text"))
    res_label.config(text=operations[operation](x, y))
    operation = ""
    last_num = ""


def point_callback():
    if "." in res_label.cget("text"):
        return
    res_label.config(text=res_label.cget("text")+".")


settings = {
    "title": "Calculadora",
    "size": {
        "w": 450,
        "h": 450
    },
    "controls": {
        "rows": 5,
        "columns": 4
    },
    "button": {
        "anchor": tk.NW,
        "relwidth": 1/4,
        "relheight": 1/5
    },
    "style": {
        "numpad": {
            "btn": {
                "bg": "gray",
                "fg": "white",
                "font": win_font
            }
        },
        "res": {
            "label": {
                "bg": "black",
                "fg": "white",
                "font": win_font
            }
        }
    },
    "operations": {
        "AC": {
            "text": "AC",
            "command": AC_callback,
            "row": 0,
            "column": 0
        },
        "+/-": {
            "text": "+/-",
            "command": change_sign_callback,
            "row": 0,
            "column": 1
        },
        "%": {
            "text": "%",
            "command": percent_callback,
            "row": 0,
            "column": 2
        },
        "/": {
            "text": "/",
            "command": gen_operation_callback("div"),
            "row": 0,
            "column": 3
        },
        "x": {
            "text": "x",
            "command": gen_operation_callback("mult"),
            "row": 1,
            "column": 3
        },
        "-": {
            "text": "-",
            "command": gen_operation_callback("sub"),
            "row": 2,
            "column": 3
        },
        "+": {
            "text": "+",
            "command": gen_operation_callback("sum"),
            "row": 3,
            "column": 3
        },
        "=": {
            "text": "=",
            "command": solve_callback,
            "row": 4,
            "column": 3
        },
        ".": {
            "text": ".",
            "command": point_callback,
            "row": 4,
            "column": 2
        }
    }
}

window.title(settings["title"])
window.minsize(settings["size"]["w"], settings["size"]["h"])

result = tk.Frame(window)
result.place(anchor=tk.NW, relwidth=1, relheight=0.2)
controls = tk.Frame(window)
controls.place(anchor=tk.NW, relwidth=1, relheight=0.8, rely=0.2)

res_label = tk.Label(result, text="", **settings["style"]["res"]["label"])
res_label.place(anchor=tk.NW, relwidth=1, relheight=1)


def gen_callback(i, j):
    def callback():
        value = str((i*3)+(j+1))
        res_label.config(text=res_label.cget("text")+value)
    return callback


def place_button(button, row, column):
    button.place(
        **settings["button"],
        relx=column/settings["controls"]["columns"],
        rely=row/settings["controls"]["rows"]
    )


def create_control_button(text, command, row, column):
    button = tk.Button(
        controls,
        command=command,
        text=text,
        **settings["style"]["numpad"]["btn"]
    )
    place_button(button, row, column)


def create_number_buttons():
    for i in range(3):
        for j in range(3):
            create_control_button(
                str((i*3)+(j+1)),
                gen_callback(i, j),
                j+1, i
            )
    create_control_button(
        "0",
        gen_callback(0, -1),
        settings["controls"]["rows"]-1, 0
    )


def create_operation_buttons():
    for button in settings["operations"].values():
        create_control_button(**button)


create_number_buttons()
create_operation_buttons()

window.mainloop()
