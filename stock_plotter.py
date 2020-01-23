#
#Author: Adrian Martinez
#Description: Stock program that accepts two values. The user decides the format for the printed
# output with the first input. The output mode will either be a horizontal or vertical plot orientation.
# The second input is a string of alternating letters and numbers. This string will specify how the plot
# will be drawn.
#

input_check = 0                     # Variable used to check user input
while input_check == 0:             # Loop used to verify input until input matches
    mode = input('Enter stock plotter mode:\n')     # User input for desired output
    if mode == 'vertical' or mode == 'horizontal':  # Used to verify input
        input_check += 1            # If input matches expected input, exits loop

while input_check > 0:
    stock_string = input('Enter stock plot input string:\n')
    if (len(stock_string)) % 2 == 0:
        input_check = 0
                                     # Inserts into proper loop depending on user input
if mode == 'vertical':               # User specified vertical plot orientation
    i = 0                            # Index variable for input on plot position
    print('#' * 19)
    plot_point = 8                   # Starting position of points, in the middle of the graph
    while i < int(len(stock_string)):# Loop until end of user input string
        if stock_string[i] == 'u':   # Adds to plot position point if indicated 'up'
            i += 1                   # Add one to index variable to jump to next position
            plot_point = plot_point + int(stock_string[i])  # Modifying starting position of point
            print('#'                                       #    by adding integer from user input
                  + ' ' * plot_point            # Left spacing
                  + '*'                         # Plot point
                  + ' ' * (16 - plot_point)     # Right spacing
                  + '#')
            i += 1                              # Add one to index to jump to next string position
        else:
            i += 1
            plot_point = plot_point - int(stock_string[i])
            print('#'
                  + ' ' * plot_point
                  + '*'
                  + ' ' * (16 - plot_point)
                  + '#')
            i += 1
    print('#' * 19)
else:                                   # User specified a horizontal plot orientation
    print('#' * (len(stock_string) // 2 + 4)) # Prints top string
    row = 17                            # Variable to run outer while loop
    while row >= 1:                     # Loop runs from top to bottom row
        row_string = ''                 # Initial value of printed string
        plot_point = 9                  # Start point for row_string position
        i = 0                           # Index variable for input on plot position
        while i < len(stock_string):    # Loop runs until it reaches end of the input string
            if stock_string[i] == 'u':  # Runs through string adding or subtracting position
                plot_point = plot_point + int(stock_string[i+1])
            else:
                plot_point = plot_point - int(stock_string[i+1])
            if plot_point == row:       # If final position is equal to the current row, * is
                row_string += '*'       #    added to printing row string
            else:
                row_string += ' '       # If position is empty, a space is added to printing string
            i += 2                      # 2 added to index variable to jump to next string position
        print('# '                      # Prints current row string
             + row_string
             + ' #')
        row -= 1                        # removes one from row variable to drop to next row
    print('#' * (len(stock_string) // 2 + 4)) #Prints bottom string