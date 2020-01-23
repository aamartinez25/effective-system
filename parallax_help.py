import os, sys

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics
import random

def main():
    gui = graphics(400, 400, 'Triangles')
    triangle_one = randomise_color(gui)
    triangle_two = randomise_color(gui)
    triangle_three = randomise_color(gui)


    while True:
        gui.clear()
        draw_triangles(triangle_one, triangle_two, triangle_three, gui)
        gui.update_frame(30)





def draw_triangles(first_color, second_color, third_color, gui):
    '''
    This function accepts the gui object and three colors.  It draws cross hairs for reference.
    when the mouse is at the center of the screen, all three triangles line up.  The canvas is
    200 x 200.  Each triangle position is offset by its scale. x1 position is
    200 - canvas_height/scale_1 = (200 - 200/10) = 180.  Then I added x/scale to get it to move.
    '''
    gui.line(0, 200, 400, 200, 'black')
    gui.line(200, 0, 200, 400, 'black')
    x = gui.mouse_x
    y = gui.mouse_y
    scale_1 = 10
    scale_2 = 5
    scale_3 = 2
    gui.triangle(x/scale_1 + 180, y/scale_1 + 155, x/scale_1 + 205, y/scale_1 + 205, x/scale_1 + 155, y/scale_1 + 205, first_color)
    gui.triangle(x/scale_2 + 160, y/scale_2 + 135, x/scale_2 + 185, y/scale_2 + 185, x/scale_2 + 135, y/scale_2 + 185, second_color)
    gui.triangle(x/scale_3 + 100, y/scale_3 + 75, x/scale_3 + 125, y/scale_3 + 125, x/scale_3 + 75, y/scale_3 + 125, third_color)


def randomise_color(gui):
    '''
    This function generates a random color each time it is called. It accepts the gui object.
    '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = gui.get_color_string(red, green, blue)
    return color

main()