''' File: build_map.py
    Author: Adrian Martinez
    Purpose of program: Program creates a cypher map based on user input
    file. Map contains only from and to characters, both single characters.

    Course no., semester: CSC 120, Spring 2020
'''

def main():
    file_name = input('file: ')
    map_set = build_map(file_name)
    is_set_valid = is_valid_map(map_set)

def build_map(file_name):
    file_name.strip()
    map_set = set()
    with open(file_name) as map_original:
        for lines in map_original:
            if lines.strip() and lines[0] != '#':
                temp_var = lines.strip().split()
                assert len(temp_var) == 2
                assert len(temp_var[0]) and len(temp_var[1]) == 1
                assert temp_var[0] not in map_set
                map_set.add(temp_var)
    return map_set

def is_valid_map(map_set):
    is_set_valid = True
    temp_set  = set()
    for subs in map_set:
        for char in subs:
            if not char.isalpha():
                is_set_valid = False
            if len(char) != 1:
                is_set_valid = False
            if char[0] in temp_set:
                is_set_valid = False
            if char[0] not in temp_set:
                temp_set.add(char[0])
    return is_set_valid

if __name__ == '__main__':
    main()
