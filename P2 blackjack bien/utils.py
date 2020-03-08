from os import system


def is_convertible(type_, val):
    try:
        type_(val)
        return True
    except Exception:
        return False


def safe_input(
        verifier,
        msg="",
        errmsg="Ingrese algo válido",
        loop=True,
        type_=str
):
    val = input(msg)
    while loop and not is_convertible(type_, val) and not verifier(type_(val)):
        val = input(errmsg)
    return type_(val)


def typed_input(type_, msg="", errmsg="Ingrese algo válido", loop=True):
    val = input(msg)
    while loop and not is_convertible(type_, val):
        val = input(msg)
    return type_(val)


def clear_screen():
    system("cls")
