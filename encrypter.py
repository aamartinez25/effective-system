#
# Author: Adrian Martinez
# Description: Program encrypts line of user designated text file by switching two randomized
# index positions. Entire list is randomized a total of the sum of five and a total of the lines
#
import random
def main():
    random.seed(125)
    index = []
    user_file = input('Enter a name of a text file to encrypt:\n')
    file_log = open(user_file, 'r') # Opens user designated text file
    file_lst = file_log.readlines() # Sets text file into a list
    file_log.close()
    for i in range(len(file_lst)):
        index.append(int(i + 1))                # Creates list line index
        file_lst[i] = file_lst[i].strip('\n')   # Strips escape sequence from list
    for i in range(len(file_lst)*5):            # Iterates randomizer five times line count
        rand_1 = random.randint(0, len(file_lst) - 1)   # First random number
        rand_2 = random.randint(0, len(file_lst) - 1)   # Second random number
        # randomizer replaces first number index with second number index
        file_lst[rand_1], file_lst[rand_2] = file_lst[rand_2], file_lst[rand_1]
        index[rand_1], index[rand_2] = index[rand_2], index[rand_1]
    new_file = open('index.txt', 'w')           # Creates save file of encryption key
    for i in range(len(index)):
        index[i] = str(index[i]) + '\n'         # Adds list to new file and appends \n
        new_file.write(index[i])
    new_file.close()
    new_file = open('encrypted.txt', 'w')
    for i in range(len(file_lst)):
        file_lst[i] = str(file_lst[i]) + '\n'
        new_file.write(file_lst[i])
    new_file.close()
main()