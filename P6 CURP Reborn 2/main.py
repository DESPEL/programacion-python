import tkinter as tk
from usuario import Usuario


class EntryPlaceholder(tk.Entry):
    def __init__(self, master, placeholder, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.insert("1", placeholder)


window = tk.Tk()
window.minsize(200, 250)
window.title("Generación y guardado de CURP")
input_widgets = {}

instructions = tk.Label(
    master=window,
    text="Ingrese sus datos"
)
instructions.pack()

input_info = {
    "nombre": "Nombre",
    "apellido_paterno": "Apellido paterno",
    "apellido_materno": "Apellido materno",
    "sexo": "Sexo (H/M)",
    "dd_nacimiento": "Dia de nacimiento(dd)",
    "mm_nacimiento": "Mes de nacimiento(mm)",
    "yyyy_nacimiento": "Año de nacimiento(aaaa)",
    "estado": "Estado de nacimiento",
}

for key, placeholder in input_info.items():
    input_widgets[key] = EntryPlaceholder(
        window,
        placeholder
    )
    input_widgets[key].pack()


def save_user():
    Usuario(
        input_widgets["nombre"].get(),
        input_widgets["apellido_paterno"].get(),
        input_widgets["apellido_materno"].get(),
        input_widgets["sexo"].get(),
        [
            int(input_widgets["dd_nacimiento"].get()),
            int(input_widgets["mm_nacimiento"].get()),
            int(input_widgets["yyyy_nacimiento"].get())
        ],
        input_widgets["estado"].get(),
    ).save()


submit_btn = tk.Button(
    window,
    text="Guardar datos y CURP",
    command=save_user,
    borderwidth=2
)
submit_btn.pack()

window.mainloop()
