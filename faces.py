def face(gui, x, y):
    gui.ellipse(x, y, 100, 100, 'red')
    gui.ellipse(x-20, y-20, 20, 20,'yellow')
    gui.ellipse(x+20, x-20, 20, 20, 'yellow')