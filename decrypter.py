#
# Author: Adrian Martinez
# Description: Program takes user designated encrypted file and index file. Program uses index
# file to decrypt text file. Program uses index file to rearrange input text file into original
# order
#

def main():
    text_file = input('Enter the name of an encrypted text file:\n')
    index_file = input('Enter the name of the encryption index file:\n')
    text_list = open(text_file, 'r').readlines() # Sets text file into a list
    index_list = open(index_file, 'r').readlines()
    for i in range(len(index_list)):
        index_list[i] = index_list[i].strip('\n')   # Strips escape sequence from list
        index_list[i] = int(index_list[i])          # Sets index file into a list as integers
    for number in range(1, len(index_list)):        # Iterates through index list
        value = index_list[number]          # sets secondary test value
        text = text_list[number]
        temp_number = number - 1            # sets comparative test value
        # iterates through values comparing two set values
        while temp_number > -1 and index_list[temp_number] > value:
            # replaces old with new value
            index_list[temp_number + 1] = index_list[temp_number]
            text_list[temp_number + 1] = text_list[temp_number]
            temp_number -= 1
        index_list[temp_number + 1] = value # sets new test value
        text_list[temp_number + 1] = text
    new_file = open('decrypted.txt', 'w')  # Creates save file of encryption key
    for i in range(len(index_list)):
        new_file.write(text_list[i])       # Writes list line by line
    new_file.close()

main()