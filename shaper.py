#
# Author: Adrian Martinez
# Description: program prints out several shapes together to create either a plumb bob,
# a house, or an hourglass. User inputs desired shape and character to make up shape
#

def up_arrow(character):
    '''
    utilizes input to create a up arrow made of user specified character
    :param character: user specified character
    :return: none
    '''
    i = 0   # index variable to control total loop count and printed characters
    row_space = 5   # controls spacing on left side of arrow
    while i < 6:
        print(' ' * row_space           # Left side spacing
              + character * (i + 1)     # Left side characters
              + character * (i * 1))    # Right side characters
        i += 1
        row_space -= 1

def down_arrow(character):
    '''
    Utilizes input to create a down arrow made of user specified character
    :param character: user specified character
    :return: none
    '''
    i = 0   # Index variable to control total loop count and printed characters
    row_space = 0   # Controls spacing on left side of arrow
    while i < 6:
        print(' ' * row_space           # Left side spacing
              + character * (6 - i)     # Left side characters
              + character * (5 - i))    # Right side characters
        i += 1
        row_space += 1

def center(height):
    '''
    Utilizes input to create a table of width, with user specified height
    :param height: total rows of printed output
    :return: none
    '''
    i = 0   # Index variable to control total loop count
    while i < height:   # Loop will continue until index variable reaches user specified row count
        print('|---------|')
        i += 1

def main():
    shape = input('Enter shape to display:\n')
    character = input('Enter arrow character:\n')
    height = int(input('Enter row-area height:\n'))
    print()
    if shape == 'hourglass':    # prints out an hourglass shape
        center(height)
        down_arrow(character)
        up_arrow(character)
        center(height)
    if shape == 'plumbbob':     # Prints out a plumb bob shape
        up_arrow(character)
        center(height)
        down_arrow(character)
    if shape == 'house':        # Prints out a house shape
        up_arrow(character)
        center(height)

main()