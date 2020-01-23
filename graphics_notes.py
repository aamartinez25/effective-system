
#moving blue block
gui = canvas
x_coord = -50
import

while True:
    gui.clear()
    gui.rectanble(x_coord, 125, 50,50,'blue')
    # to reset
    if x_coord == 500:
        x_coord = -50

    gui.update_frame(60)
    x_coord += 5


gui.mouse_x
gui.mouse_y

