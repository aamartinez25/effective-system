#
#Author: Adrian Martinez
#Description: Program that creates a tie fighter with user input width
#
width = int(input('Enter TIE width: \n'))

center_width = '         '

print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '/==---==\\' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + '\\==---==/' + ' ' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')