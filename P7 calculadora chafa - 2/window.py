import tkinter as tk

from controls import Controls
from result import Result


class Window:
    def __init__(self, master):
        self.window = master

        self._create_frames()

    def _create_frames(self):
        self._create_result_frame()
        self._create_controls_frame()

    def _create_result_frame(self):
        self.result = Result(self.window)

    def _create_controls_frame(self):
        self.controls = Controls(self.window, self.result.label)
