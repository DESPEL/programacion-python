import tkinter as tk

import config

from controller import Controller
from user_list_page import FolderListFrame
from editar_nota import NoteFrame
from notes_page import NotesFrame


window = tk.Tk()
window.minsize(config.WIDTH, config.HEIGHT)
window.resizable(False, False)

controller = Controller()
controller.set_pages({
    "folder_list": FolderListFrame(controller, window),
    "notes_frame": NotesFrame(controller, window),
    "note_frame": NoteFrame(controller, window)
})
controller.init_pages()

controller.show("folder_list")
window.mainloop()
