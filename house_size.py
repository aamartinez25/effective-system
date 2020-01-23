#print('Here\'s a size 3 house')
#print(' ___^___ ')
#print('/       \\')
#print('|   H   |')
#print('|___H___|')

house_size = int(input('What size house should be printed? \n'))

print('Here\'s a size', house_size, 'house')
print(' ' + '_' * house_size + '^' + '_' * house_size + ' ')
print('/' + ' ' * house_size + ' ' + ' ' * house_size + '\\')
print('|' + ' ' * house_size + 'H' + ' ' * house_size + '|')
print('|' + '_' * house_size + 'H' + '_' * house_size + '|')

