last_num = ""
operation = ""


def get_operation_buttons_settings(res_label):
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

    return {
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
