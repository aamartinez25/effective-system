def main():
    contact_file = open('contacts.txt', 'r')
    contact_lst = contact_file.readlines()
    contact_set = set()
    for n in contact_lst:
        line = n.strip('\n').split(' | ')
        contact_set.add(tuple(line))
    print('Welcome to the contacts app!')
    ex_code = False
    while not ex_code:
        command  = input('>\n')
        if command == 'add contact':
            contact_set = add_contact(contact_set)
        elif 'show contacts with' in  command:
            show_contact(contact_set, command)
        elif command == 'exit':
            ex_code = True
        else:
            print('huh?')
    print('Goodbye!')


def show_contact(contact_set, command):
    matches = set()
    for word in command:
        user_input = word.split()
        temp_info = user_input[4:]
        if len(temp_info) > 1:
            temp_info = temp_info[0] + temp_info[1]
    for contacts in contact_set:
        if temp_info.issubset(contact_set):
            matches.add(contacts)
    for contacts in sorted(matches):
        print(temp_info + '\'s contact info: \n')
        print('email:', contacts[1], '\n')
        print('phone:', contacts[2], '\n')

main()