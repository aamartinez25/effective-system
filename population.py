''' File: strings_and_input.py
    Author: Adrian Martinez
    Purpose of program: program uses user input file to output states and
    corresponding populations. Output is states print out with their
    populations with a tally printed out at the end
    Course no., semester: CSC 120, Spring 2020
'''

def main():
    file_name = input('file: ')
    file_name.strip()
    states_original = open(file_name, 'r').readlines()
    state_lst = []
    temp_var = ''
    population = 0
    for i in range(len(states_original)):
        temp_lst = states_original[i].strip('\n').split()
        if len(temp_lst) > 0:
            temp_var = temp_lst[0]
        if temp_var[0] != '#' and temp_lst != []:
            state = ' '.join(temp_lst[:-1])
            state_lst.append(state)
            population += int(temp_lst[-1])
            print('State/Territory: '+ state)
            print('Population: \t', str(temp_lst[-1])+ '\n')
    print('# of States/Territories:',len(state_lst))
    print('Total Population:\t',str(population))

if __name__ == '__main__':
    main()