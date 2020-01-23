#
# Author: Adrian Martinez
# Description: Program converts non-english words to their english form. Program accepts two
# inputs via console.
#

def main():
    converter = {}          # Dictionary holding words from file with defined keys/values
    file_name = input('Enter name of words file:\n')
    text_file = open(file_name, 'r').readlines()
    for line in text_file:
        words = line.strip('\n').split(',')
        for i in range(1, len(words)):
            converter[words[i]] = words[0]      # creates a key for every first list value
    word_input = input('Enter word to convert to English:\n')   # User input word to check
    print()
    if word_input in converter:
        print('English version is: ' + str(converter[word_input]))  # Checks input word against keys
    else:
        print('Not sure.')

main()