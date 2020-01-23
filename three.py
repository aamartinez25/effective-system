#
# Author: Adrian Martinez
# Description: Program draws three shapes that move from left to right in a column. After each
# iteration the shapes start on a new random row.
#

import os, sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics
import random

def main():
    x_coord = -50   # Global variables for shape coordinates
    rectangle_y = 0
    ellipse_y = 0
    triangle_y = 0
    rectangle_y, ellipse_y, triangle_y = randomizer(ellipse_y,
                                                    rectangle_y, triangle_y) # Randomizer function
    gui = graphics(500, 500, 'three')   # Canvas parameters
    while True:                         # Loop set
        gui.clear()                     # Clears canvas
        gui.triangle(x_coord, triangle_y, x_coord + 50, triangle_y, x_coord + 25,   # Triangle draw
            triangle_y - 50, 'blue')
        gui.ellipse(x_coord + 25, ellipse_y, 50, 50, 'goldenrod2')    # Ellipse draw
        gui.rectangle(x_coord, rectangle_y, 50, 50, 'green')    # Rectangle draw
        if x_coord > 500:               # Shape x-coords reset after reaching 500
            x_coord = -50               # x-coords reset to -50 starting point
            rectangle_y, ellipse_y, triangle_y = randomizer(rectangle_y, ellipse_y, triangle_y)
        gui.update_frame(40)
        x_coord += 5

def randomizer(ellipse_y, rectangle_y, triangle_y):
    '''
    function used to randomize the y-coordinates of the three shapes.
    :param ellipse_y: parameter for the y-coordinate of the ellipses point
    :param rectangle_y: parameter for the y-coordinate of the top-left rectangle point
    :param triangle_y: parameter for the y-coordinates of the triangle's points
    :return: randomized y-coordinate points
    '''
    rectangle_y = random.randint(0,500)     # Randomized point between 0 and 500
    ellipse_y =  random.randint(0,500)
    triangle_y = random.randint(0,500)
    return rectangle_y, ellipse_y, triangle_y

main()