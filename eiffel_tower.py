#
#Author: Adrian Martinez
#Description: print out ASCII-art of the White House with user designated proportions
#

size = int(input('Enter Eiffel tower size:\n'))

upper_height = size * 1.5
u_h = int(upper_height)
middle_width = size * 2 + 1
middle_height = size / 2 + 3
m_w = int(middle_width)
m_h = int(middle_height)
lower_width = size * 4 + 1
lower_height = size / 1.5
l_w = int(lower_width)
l_h = int(lower_height)
upper_space = lower_width / 2 + 2
u_s = int(upper_space)
middle_space = lower_width / 4 + 2
m_s = int(middle_space)
print()
print(' ' * u_s + ' $ ')
print((' ' * u_s + '|Z|\n' )* u_h, end = '')
print(' ' * m_s + '/' + 'Z' * m_w + '\\')
print((' ' * m_s  + 'H' + ' ' * m_w + 'H\n') * m_h, end = '')
print(' ' * 2 + '/' + '%' * l_w + '\\')
print((' ' + '##' + ' ' * l_w + '##\n') * l_h, end = '')
print(('##' + ' ' * (l_w + 2) + '##\n') * l_h, end = '')