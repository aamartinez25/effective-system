''' File: swap.py
    Author: Adrian Martinez
    Purpose of program: program takes an input string and swaps positions of first and second
    half characters
    Course no., semester: CSC 120, Spring 2020
'''

def main():
    user_inp = input('Please give a string to swap: ')
    user_inp.strip()
    length = len(user_inp)
    temp_str = ''
    if len(user_inp)%2==0:
        for i in range((length//2), length ):
            print(user_inp[i], end = '')
        for i in range(0, length//2):
            print(user_inp[i], end = '')
    else:
        for i in range((length//2)+1, length):
            temp_str += user_inp[i]
        temp_str += user_inp[length//2]
        for i in range(0, (length//2)):
            temp_str += user_inp[i]
        print(temp_str)

if __name__ == '__main__':
    main()