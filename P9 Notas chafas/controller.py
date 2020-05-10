import tkinter as tk


class UnknownFrame(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"El frame no existe: {self.message}"
        else:
            return f"Frame no existe"


class Controller:
    def __init__(self, frame_dict={}):
        self.frames = frame_dict
        self.last_call = None

    def set_pages(self, frame_dict):
        self.frames = frame_dict

    def show(self, name, *args, **kwargs):
        if name not in self.frames.keys():
            raise UnknownFrame()

        self.frames[name].tkraise()

        if self.last_call is not None and hasattr(self.last_call, "on_hide"):
            self.last_call.on_hide()

        if hasattr(self.frames[name], "update"):
            self.frames[name].update(*args, **kwargs)

        self.last_call = self.frames[name]

    def init_pages(self):
        for page in self.frames.values():
            page.place(anchor=tk.NW, relwidth=1, relheight=1)
