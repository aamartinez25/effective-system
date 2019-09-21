#
#Author: Adrian Martinez
#Description: Program takes a string input of zero through nine and outputs
# bars of center aligned hashtags starting with the users first input and going
# through remaining digit outputs. First two inputs are added together to create
# a line.
#
bars = input('Enter bar string:\n')                 #user bar string input

index = 0
bar_height = len(bars) -1                           #Variable used to determine how many bars will be printed

print('+------------------+')
while index <= bar_height:                          #While loop used to print out hashtag bars
    bar_length_left = '#' * int(bars[index])        #Variable for printed bar hashtags from user inputs
    bar_length_right = '#' * int(bars[index + 1])   #Variable for using next input
    space_left = ' ' * (9 - int(bars[index]))       #Variable for spacing
    space_right = ' ' * (9 - int(bars[index + 1]))  #Variable for using next string as base for right side spacing
    print('|' + space_left +  bar_length_left + bar_length_right + space_right + '|\n', end = '')
    index += 2
print('+------------------+')
