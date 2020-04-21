import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk

window = tk.Tk()

win_font = tkFont.Font(family="Arial", size="20")

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
        }
    },
    "operations": {
        "AC": {
            "text": "AC",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 0,
            "column": 0
        },
        "+/-": {
            "text": "+/-",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 0,
            "column": 1
        },
        "%": {
            "text": "%",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 0,
            "column": 2
        },
        "/": {
            "text": "/",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 0,
            "column": 3
        },
        "x": {
            "text": "x",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 1,
            "column": 3
        },
        "-": {
            "text": "-",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 2,
            "column": 3
        },
        "+": {
            "text": "+",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 3,
            "column": 3
        },
        "=": {
            "text": "=",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 4,
            "column": 3
        },
        ".": {
            "text": ".",
            "command": lambda x: print("lul"), # TODO: FUNC
            "row": 4,
            "column": 2
        }  
    }
}

window.title(settings["title"])
window.minsize(settings["size"]["w"], settings["size"]["h"])
