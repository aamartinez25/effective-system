#
#Author: Adrian Martinez
#Description: Program that creates a tie fighter with user input width
#

width = int(input('Enter TIE width: /n')) #initial width input from user
center_width = '         ' #var for center tie width

print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '/==---==\\' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + '\\==---==/' + ' ' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')
print('|[' + ' ' * width + center_width + ' ' * width +']|')
