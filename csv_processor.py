#
# Author: Adrian Martinez
# Description: program reads csv file with no column labels and can compute maximum, minimum of a
# column.
#

def main():
    commands = {
        'min': minimum,
        'max': maximum,
        'avg': average
    }
    csv_file = input('Enter CSV file name:\n')
    csv_lst = []
    for line in csv_file:
        col = line.split(',')
        csv_lst.append(col)
    col_input = input('Enter column number: \n')
    col_op = input('Enter column operation:\n')
    if col_op in commands:
        func = commands[col_op]
        func(csv_lst, col_input)
    else:
        print('Command not found.')

def minimum(csv_lst, col_input):
    comparison = 9999999
    for n in csv_lst[col_input]:
        if n < comparison:
            comparison = n
    return comparison

def maximum(csv_lst, col_input):
    comparison = 0
    for n in csv_lst[col_input]:
        if n > comparison:
            comparison = n
    return comparison

def average(csv_list, col_input):
    total = 0
    for n in csv_list[col_input]:
        total += n
    aver = total / len(csv_list[col_input])
    return aver

main()