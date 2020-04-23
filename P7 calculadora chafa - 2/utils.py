def get_label_text(label):
    return label.cget("text")


def set_label_text(label, text):
    label.config(text=text)
