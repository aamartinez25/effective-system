#
# Author: Adrian Martinez
# Description: Program displays a landscape in a graphics canvas and allows the user to control
# the perspective of the landscape by moving the mouse. Birds don't move, sorry, had enough
# trouble with the rest of the program, surprised I got this far.
#

import os, sys

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics
import random


def main():
    gui = graphics(500, 500, 'Landscape')  # Canvas parameters
    mountain_a = random_color(gui)  # Function calls for randomised mountain color
    mountain_b = random_color(gui)
    mountain_c = random_color(gui)
    while True:                     # Keeps main function running in a loop
        gui.clear()                 # clears canvas
        landscape_draw(mountain_a, mountain_b, mountain_c, gui) # Draws background landscape
        i = 0
        while i < 5:                # Draws five birds
            birds(i, gui)
            i += 1
        gui.update_frame(40)


def random_color(gui):
    '''
    Function generates randomised color string
    :param gui: gui object used as input parameter to create color for the mountains
    :return: color: rgb string for mountain color
    '''
    red = random.randint(0, 255)    # Random number generated for RGB
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = gui.get_color_string(red, green, blue)
    return color


def landscape_draw(mountain_a, mountain_b, mountain_c, gui):
    '''
    Function generates background image of three mountains, the sun, grass and a tree.
    :param mountain_a: randomised color for mountain a
    :param mountain_b: randomised color for mountain b
    :param mountain_c: randomised color for mountain c
    :param gui: imported object to allow the drawing of shapes on the canvas
    :return: none
    '''
    x = gui.mouse_x         # Mouse input
    y = gui.mouse_y
    i = -50
    gui.rectangle(-10, -10, 550, 550, 'DeepSkyBlue2')
    gui.ellipse(x / 30 + 400, y / 30 + 50, 50, 50, 'yellow')
    gui.triangle(x / 15 + 150, y / 15 + 400, x / 15 + 375, y / 15 + 400, x / 15 + 250, y / 15 +
                 100, mountain_a)
    gui.triangle(x / 13 + -50, y / 13 + 400, x / 13 + 350, y / 13 + 400, x / 13 + 150, y / 13 +
                 150, mountain_b)
    gui.triangle(x / 10 + 220, y / 10 + 400, x / 10 + 550, y / 10 + 375, x / 10 + 375, y / 10 +
                 150, mountain_c)
    gui.rectangle(x / 15 + -50, y / 15 + 375, x / 15 + 550, y / 15 + 300, 'Lawn Green')
    while i < 500:
        gui.line(x / 15 + i, y / 15 + 375, x / 15 + i, y / 15 + 350, 'Lawn Green', 3)
        i += 7
    gui.rectangle(x / 15 + 375, y / 15 + 345, 20, 50, 'brown')
    gui.ellipse(x / 15 + 385, y / 15 + 325, 45, 90, 'green')

def birds(i, gui):
    '''
    Function prints out a single bird, maintaining offset between each loop
    :param i: parameter used to increase offset from original point
    :param gui: allows drawing on canvas
    :return: none
    '''
    offset = i * 40
    bird_x = 50
    bird_y = 50
    gui.line(bird_x + offset, bird_y + offset, (bird_x + 20) + offset, (bird_y + 20) + offset,
             'black', 3)
    gui.line((bird_x + 20) + offset, (bird_y + 20) + offset, (bird_x + 40) + offset, bird_y +
             offset, 'black', 3)

main()