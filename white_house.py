#
#Author: Adrian Martinez
#Description: print out ASCII-art of the White House with user designated proportions
#

side_width = int(input('Specify side width: \n'))
middle_width = int(input('Specify middle width: \n'))
flag_height = int(input('Specify flag height: \n'))

side_width_print = side_width * 3 #Var. to decrease clutter on flag function
middle_width_print = middle_width * 4

print()
print(' ' * (side_width_print + middle_width_print + 1) + '|##')  #top of flag
print((' ' * (side_width_print + middle_width_print + 1) + '|\n') * flag_height, end = '')#Flag Pole

print(' ' * (side_width_print + 1) + '.-.-' * middle_width + "\'\'" + '-.-.' * middle_width)
print(' ' * (side_width_print + 1) + ';.__' * middle_width + "--" + '__.;' * middle_width)

#Top of White House
print('.' + '___' * side_width + '[---' * middle_width + "--" + '---]' * middle_width +
      '___' * side_width + '.')

#Middle of White House
height = int((side_width + middle_width) / 4) + 1

print((('|' + 'II ' * side_width + '||II' * middle_width + 'HH' + 'II||' * middle_width +
        ' II' * side_width + '|\n') + #Second Floor

      ('|' + '.. ' * side_width + '||..' * middle_width + '||' + '..||' * middle_width +
       ' ..' * side_width + '|\n')) * height, end = '') #First Floor

