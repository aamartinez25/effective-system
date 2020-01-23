#
# Author: Adrian Martinez
# Description: program that makes an avatar, either one of three premade avatars, or a custom avatar.
# User input can select avatar's hat style, hair style, eye style, arm style, length of the torso,
# length of the legs, and shoe style.
#

def main():
    print('----- AVATAR -----')
    avatar = input('Select an Avatar or create your own:\n') # User input determining avatar style
    while avatar != 'Jeff' and avatar != 'Adam' and avatar != 'Chris' \
            and avatar != 'custom' and avatar != 'exit': # Loop until user uses proper input
        avatar = input('Select an Avatar or create your own:\n')
    if avatar == 'Jeff':        # If user selects a premade avatar,
        hat_style = 'both'      # setting parameters to preset values
        hair_style = True
        eye_style = '0'
        arm_style = '='
        torso_length = 2
        leg_height = 2
        shoe_style = '#HHH#'
    elif avatar == 'Adam':
        hat_style = 'right'
        hair_style = False
        eye_style = '*'
        arm_style = 'T'
        torso_length = 3
        leg_height = 3
        shoe_style = '<|||>'
    elif avatar == 'Chris':
        hat_style = 'front'
        hair_style = True
        eye_style = 'U'
        arm_style = 'W'
        torso_length = 1
        leg_height = 4
        shoe_style = '<>-<>'
    if avatar == 'custom':  # If user selects custom avatar, user inputs desired inputs here
        print('Answer the following questions to create a custom avatar')
        hat_style = input('Hat style ?\n')
        eye_style = input('Character for eyes ?\n')
        hair_style = input('Shaggy hair (True/False) ?\n')
        arm_style = input ('Arm style ?\n')
        torso_length = int(input('Torso length ?\n'))
        leg_height = int(input('Leg length (1-4) ?\n'))
        shoe_style = input('Shoe look ?\n')
    if hair_style == 'True':    # Setting hair style to bool, because I didn't realize until \
        hair_style = True       # I was done that it was easier just to compare strings
    elif hair_style == 'False':
        hair_style = False
    if avatar == 'exit':        # If user decides to exit program, function exits here using return
        return

    hat(hat_style)          # Functions to print out avatar sections with user designated parameters
    hair(hair_style)
    face(avatar, eye_style)
    arms(arm_style)
    torso(torso_length)
    legs(leg_height, shoe_style)

def hat(hat_style):
    '''
    function prints out user designated hat.
    :param hat_style: parameter designated by user, choosing which way hat faces
    :return: none
    '''
    hat_index = '___/_______\___'   # local index variable to set initial hat style
    print('\n       ~-~\n     /-~-~-\\')    # Prints out top of hat
    if hat_style == 'left':
        print(' ' + hat_index[1:12])        # Uses string slice from hat index variable
    if hat_style == 'right':
        print('    ' + hat_index[3:15])
    if hat_style == 'both':
        print(' ' + hat_index)
    if hat_style == 'front':
        print('    ' + hat_index[3:12])

def hair(hair_style):
    '''
    function prints out user designated hair style.
    :param hair_style: parameter designated by user, choosing whether avatar has shaggy hair or not
    :return: none
    '''
    if not hair_style:
        print("    |'''''''|")  # Non-shaggy hair
    else:
        print('    |"""""""|')  # Shaggy hair

def face(avatar, eye_style):
    '''
    function prints out avatar's face with user designated eye style
    :param avatar: parameter to designate if avatar has a neck with premade style
    :param eye_style: parameter designated by user, choosing avatar eye style
    :return: none
    '''
    print('    | ' + eye_style + '   ' + eye_style + ' |')  # Prints out avatar with user \
    print('    |   V   |')                                  # designated eye style
    print('    |  ~~~  |')
    print('     \_____/')

    if avatar == 'Adam' or avatar == 'Chris':   # Prints out neck on premade avatar
        torso_length = 1
        torso(torso_length)

def arms(arm_style):
    '''
    function prints out avatar's arms with user designated arm style
    :param arm_style: parameter to designate avatar arm style
    :return: none
    '''
    arm_length = 4
    arm_return = ''         # Local variable to set full arm set
    i = 0
    while i < arm_length:   # Loops until arm print variable reaches desired length
        arm_return += arm_style
        i += 1
    print(' 0' + arm_return + '|---|' + arm_return + '0 ')

def torso(torso_length):
    '''
    function prints out avatar's torso
    :param torso_length: parameter set by user designating avatar torso length
    :return: none
    '''
    i = 1
    while i <= torso_length:    # Loops until proper torso length is reached
        print('      |-X-|')
        i += 1

def legs(leg_height, shoe_style):
    '''
    function prints out avatar's legs and shoes
    :param leg_height: parameter set by user designating avatar leg length
    :param shoe_style: parameter set by user designating avatar's shoe style
    :return: none
    '''
    print('      HHHHH')
    i = 0
    inside_space = ' '          # Local variable indexing space inside avatar's legs
    outside_space = '     '     # Local variable indexing space outside avatar's legs
    spacing_index = 5
    while i < leg_height:
        print(outside_space + '///' + inside_space + '\\\\\\')
        outside_space = outside_space[1:spacing_index]
        inside_space += '  '
        spacing_index += 1
        i += 1
    print(shoe_style + '       ' + shoe_style)

main()