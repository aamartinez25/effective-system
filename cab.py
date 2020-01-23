#
#Author: Adrian Martinez
#Description: Program takes a string input of zero through nine and outputs
# bars of right aligned hashtags starting with the users first input and going
# through remaining digit outputs
#
bars = input('Enter bar string:\n')         #user string input
i = 0
print('+------------------+')
while i < len(bars):
    print('|'
          + (9 - int(bars[i])) * ' '        # Left Spacing
          + int(bars[i]) * '#'              # Left Hashes
          + int(bars[i + 1]) * '#'          # Right Hashes
          + (9 - int(bars[i + 1])) * ' '    # Right Spacing
          + '|')
    i += 2 # Each Row corresponds to a pair of inputs, skip two to proceed to next row
print('+------------------+')

