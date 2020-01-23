#
#Author: Adrian Martinez
#Description: print out ASCII-art of the Bodiam castle with user designated width
#
width = int(input('castle width: \n'))

center_width_top = '.-.-.'
center_width_mid = '|-.-|'
center_width = '| H |'
center_width_bottom = '||^||'

print()
print('   ' + " " * width + center_width_top + ' ' * width + '   ')
print('[-]' + " " * width + center_width_mid + ' ' * width + '[-]')
print('| |' + "_" * width + center_width + '_' * width + '| |')
print('| |' + " " * width + center_width + ' ' * width + '| |')
print('| |' + " " * width + center_width + ' ' * width + '| |')
print('|_|' + "_" * width + center_width_bottom + '_' * width + '|_|')

