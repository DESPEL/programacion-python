import tkinter as tk

import config

from controller import Controller
from user_list_page import UserListFrame
from create_user_frame import CreateUserFrame
from profile_frame import ProfileFrame

window = tk.Tk()
window.minsize(config.WIDTH, config.HEIGHT)
window.resizable(False, False)

controller = Controller()
controller.set_pages({
    "user_list": UserListFrame(controller, window),
    "create_user": CreateUserFrame(controller, window),
    "profile_frame": ProfileFrame(controller, window),
})
controller.init_pages()

controller.show("user_list")

window.mainloop()
