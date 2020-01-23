#
#Author: Adrian Martinez
#Description: Program takes a string input of zero through nine and outputs
# bars of left aligned hashtags starting with the users first input and going
# through remaining digit outputs
#
bars = input('Enter bar string:\n')         #user string input
i = 0
print('+---------+')
while i < len(bars):
    print('|'
          + int(bars[i]) * '#'              # Left Hashes
          + (9 - int(bars[i])) * ' '        # Left Spacing
          + '|')
    i += 1 # Each Row corresponds to a single input, add one to proceed to next row
print('+---------+')
