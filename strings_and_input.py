''' File: strings_and_input.py
    Author: Adrian Martinez
    Purpose of program: program prints out lines depending on user input
    Course no., semester: CSC 120, Spring 2020
'''

def main():
    qwerty_lib = ['q','w','e','r','t','y', 'Q', 'W', 'E', 'R', 'T', 'Y']
    uiop_lib = ['u','i','o','p']

    user_inp = input('input string: ')

    print(len(user_inp))
    print(user_inp[1])
    print(user_inp[:10])
    print(user_inp[-5:])
    print(user_inp.upper())
    if user_inp[0] in qwerty_lib:
        print('QWERTY')
    elif user_inp[0] in uiop_lib and user_inp[0].islower():
        print ('UIOP')
    elif user_inp[0].isalpha():
        print('LETTER')
    elif user_inp[0].isnumeric():
        print('DIGIT')
    else:
        print('OTHER')

    digit1 = int(input())
    digit2 = int(input())
    print(digit1*digit2)

if __name__ == '__main__':
    main()