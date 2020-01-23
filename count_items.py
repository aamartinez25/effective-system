''' File: count_items.py
    Author: Adrian Martinez
    Purpose of program: program uses user input file to output string and
    corresponding integer count in alphabetic order
    Output is states print out with their populations with a tally printed out
    at the end
    Course no., semester: CSC 120, Spring 2020
'''

def main():
    file_name = input('File to scan: ')
    file_name.strip()
    item_lst = []
    user_file = open(file_name, 'r')
    for lines in user_file:
        temp_var = lines.strip().split()
        item_lst.append(temp_var)
    string_dic = {}
    for line in item_lst:
        if line[0] not in string_dic:
            string_dic[line[0]] = 0
        string_dic[line[0]] += int(line[1])
    new_dic = {}
    for key, value in string_dic.items():
        if value not in new_dic:
            new_dic[value] = []
        new_dic[value] += [key]

    for key in sorted(new_dic.keys(), reverse = True):
        string_list = new_dic[key]
        for string in sorted(string_list):
            print(string, key)
    
if __name__ == '__main__':
    main()