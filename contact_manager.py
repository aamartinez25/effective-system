#
# Author: Adrian Martinez
# Description: Program is a contact organizer. Program uses input file and can read and write to
# program with the option of adding new contacts and reviewing existing contacts.
#

def main():
    contact_file = open('contacts.txt', 'r')    # opens contact file
    contact_lst = contact_file.readlines()
    contact_set = set()
    for n in contact_lst:                       # strips text lines and adds to tuple set
        line = n.strip('\n').split(' | ')
        contact_set.add(tuple(line))
    print('Welcome to the contacts app!')
    ex_code = False                             # loops until user inputs exit
    while not ex_code:
        command  = input('> ')
        print('')
        if command == 'add contact':            # calls add contact function
            add_contact(contact_set)
        elif 'show contacts with' in  command:  # calls show contact function
            show_contact(contact_set, command)
        elif command == 'exit':                 # exits loop, writes new file
            save_contacts(contact_set)
            print('Goodbye!')
            return
        else:                                   # unknown command
            print('huh?')


def add_contact(contact_set):
    '''
    function adds contacts to existing set, if contact already exists, user is told
    :param contact_set: set of tuples containing existing contact information
    :return: none
    '''
    name = input('name: ')                  # new contact information
    email = input('\nemail: ')
    phone = input('\nphone: ')
    new_contact = (name, email, phone)      # sets information into a set
    if new_contact in contact_set:
        print('\nContact already exists!')  # informs user contact already exists
    else:
        print('\nContact added!')           # informs user contact added successfully
    contact_set.add(new_contact)            # adds information, if information is duplicate,
                                            # no exception is called due to set
    return

def show_contact(contact_set, command):
    '''
    function prints out contact information for user input information
    :param contact_set: set of tuples containing existing contact information
    :param command: user input information with requested contact information
    :return: none
    '''
    matches = set()                     # new set for called information
    user_input = command.split()        # splits command into a list
    temp_info = user_input[4:]          # strips excess strings
    if len(temp_info) > 1:              # if information is more than one index, concatenates
                                        # information into a single set
        temp_info_hold = {temp_info[0] + ' ' + temp_info[1]}
    else:
        temp_info_hold = set(temp_info)
    for contacts in contact_set:        # checks input information against existing contacts
        if temp_info_hold.issubset(contacts):
            matches.add(contacts)       # adds matching information to matches set
    if len(matches) < 1:                # informs user no contacts with corresponding information
        print('None')
    else:
        for contacts in sorted(matches):    # prints out matching contact information
            print(contacts[0] + '\'s contact info: ')
            print('  email:', contacts[1])
            print('  phone:', contacts[2])

def save_contacts(contact_set):
    '''
    function creates and writes file with contact information in a text file
    :param contact_set: set of tuples containing existing contact information
    :return: none
    '''
    new_file = open('contacts.txt', 'w')
    for tup in sorted(contact_set):     # writes contacts into single lines
        temp_contact = tup[0] + ' | ' + tup[1] + ' | ' + tup[2] + '\n'
        new_file.write(temp_contact)
    new_file.close()

main()