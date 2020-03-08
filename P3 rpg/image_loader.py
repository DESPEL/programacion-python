from colorama import Back
from PIL import Image

import gui

colors = {
    (12, 12, 12): Back.BLACK,
    (0, 55, 218): Back.BLUE,
    (19, 161, 14): Back.GREEN,
    (58, 150, 221): Back.CYAN,
    (197, 15, 31): Back.RED,
    (136, 23, 152): Back.MAGENTA,
    (193, 156, 0): Back.YELLOW,
    (204, 204, 204): Back.WHITE,
    (118, 118, 118): Back.LIGHTBLACK_EX,
    (59, 120, 255): Back.LIGHTBLUE_EX,
    (22, 198, 12): Back.LIGHTGREEN_EX,
    (97, 214, 214): Back.LIGHTCYAN_EX,
    (231, 72, 86): Back.LIGHTRED_EX,
    (180, 0, 158): Back.LIGHTMAGENTA_EX,
    (249, 241, 165): Back.LIGHTYELLOW_EX,
    (242, 242, 242): Back.LIGHTWHITE_EX
}


def load_image(path):
    image = Image.open(path)
    image_rgb = image.convert("RGB")
    width, height = image.size

    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image_rgb.getpixel((x, y))
            row.append((r, g, b))
        pixels.append(row)
    return pixels


def get_console_colored_image(image):
    colored_image = []
    for row in image:
        colored_row = []
        for pixel in row:
            console_color = colors.get(pixel, Back.BLACK)
            colored_row.append(gui.Pixel(console_color))
        colored_image.append(colored_row)
    return colored_image


def load_console_sprite(path):
    image = load_image(path)
    colored_image = get_console_colored_image(image)
    return gui.Image(colored_image)
