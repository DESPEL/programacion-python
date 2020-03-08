import colorama
from colorama import Back
from colors import color

from gui import GUI, Point, Image
from sprites import warrior, wizard, archer

colorama.init()

GUI.print(Point(0, 0), archer)
