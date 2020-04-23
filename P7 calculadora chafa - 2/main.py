import tkinter as tk

import settings

from window import Window

window = tk.Tk()

window.title(settings.WIN_TITLE)
window.minsize(settings.WIN_WIDTH, settings.WIN_HEIGHT)

app = Window(window)

window.mainloop()
