#
# Author: Adrian Martinez
# Description: program inputs text file and outputs an infographic based on the text, showing number of small,
# medium and large words.
#

import os, sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def main():
    file_name = input('file input name: \n')
    text_file = open(file_name, 'r').readlines()
    cap_lst, punct_lst, word_count = dict_creation(text_file)
    size_lst, unique_words = word_counts(word_count)
    output_string = ''
    for size in size_lst:
        output_string += most_used(size)
    master_lst = [size_lst, cap_lst, punct_lst]
    table(graphics, file_name, output_string, master_lst, unique_words)

def dict_creation(text_file):
    '''
    this function uses input text file to create lists and dicts. These lists count out the
    number of unique words, words with capitals and words with punctuation.
    :param text_file: user input file list
    :return: list of capitalised words, punctuated words, and unique words
    '''
    word_list = []
    word_count = {}
    capital_set = set()
    punctuation_set = set()
    for line in text_file:          # loop adds words to unique word list skipping empty lines
        if line != '\n':
            words = line.strip('\n').split(' ')
            for word in words:
                word_list.append(word)
    for words in word_list:         # adds words to unique word list, capitalised list,
                                    # and punctuated list
        if words not in word_count:
            word_count[words] = 0   # sets word as key and adds number of times used in text
            if words[0].isupper():  # checks capitalisation of word
                capital_set.add(words)
            if words[-1] in ',.?!': # checks if word contains puncuation
                punctuation_set.add(words)
        word_count[words] += 1
    cap_lst = [len(capital_set)]        # creates variable for total number of cap words
    punct_lst = [len(punctuation_set)]  # creates variable for total number of punct words
    return cap_lst, punct_lst, word_count

def word_counts(word_count):
    '''
    This function uses the unique word dictionary and creates three different lists, of small,
    medium and large words.
    :param word_count: dictionary containing unique word counts
    :return: 2d list of small, medium and large words, and total unique word count
    '''
    size_lst = []           # 2D list of all unique small, medium and large words
    unique_words = 0        # unique word count
    word_size_small = {}    # dict of small words and word count
    word_size_medium = {}   # dict of medium words and word count
    word_size_large = {}    # dict of large words and word count
    for word, values in word_count.items(): # loop iterates through determing length of word and
                                            # adds to unique word count
        if len(word) <= 4:
            word_size_small[word] = values
            unique_words += 1
        elif 5 <= len(word) <= 7:
            word_size_medium[word] = values
            unique_words += 1
        elif len(word) >= 8:
            word_size_large[word] = values
            unique_words += 1
    size_lst.append(word_size_small)    # appends word lists to master size list
    size_lst.append(word_size_medium)
    size_lst.append(word_size_large)
    return size_lst, unique_words

def most_used(size):
    '''
    function loops and determines most used small medium and large word
    :param size: row in list, either small, medium and large
    :return: output string shows most common word in a string
    '''
    biggest_number = 0
    common_word = ' '
    for word, value in size.items():
        if value > biggest_number:
            biggest_number = value
            common_word = word
    output_string = (common_word + ' (' + str(biggest_number) + 'x) ')
    return output_string

def table(graphics, file_name, output_string, master_lst, unique_words):
    '''
    function displays text file information in graphic form
    :param graphics: graphics object
    :param file_name: name of user input file
    :param output_string: string of most common small medium and large words
    :param master_lst: list containing all unique words and word counts
    :param unique_words: integer of total unique words in text
    :return: none
    '''
    gui = graphics(650, 700, 'infographic')
    gui.rectangle(0, 0, 650, 700, 'grey')
    gui.text(20, 10, file_name, 'cyan', 30)
    gui.text(20, 60, 'Total Unique Words: ', 'white', 20)
    gui.text(275, 60, unique_words, 'white', 20)
    gui.text(20, 100, 'Most Used Words(s/m/l):  ', 'white', 15)
    gui.text(245, 100, output_string, 'cyan', 15)
    length_graph(gui, master_lst, unique_words)

def length_graph(gui, master_lst, unique_words):
    '''
    function prints out bars depicting ratios of types of words
    :param gui: import from graphics object
    :param master_lst:  list containing all unique words and word counts
    :return:
    '''
    offset = 0
    width = 125
    x = int(offset * width + 25)
    row_total = unique_words
    gui.text(x, 145, 'Word lengths', 'white', 15)
    gui.rectangle(x,180,125,(450//row_total)*len(master_lst[0][0]),'blue')
    gui.text(x+5,185,'small words','white',10)
    gui.rectangle(x,180+(450//row_total)*len(master_lst[0][0]),125,(450//row_total)
                     *len(master_lst[0][1]),'green')
    gui.text(x+5,185+(450//row_total)*len(master_lst[0][0]),'medium words','white',10)
    gui.rectangle(x,180+(450//row_total)*len(master_lst[0][0])+(450//row_total)
                     *len(master_lst[0][1]),125,(450//row_total)*len(master_lst[0][2]),'blue')
    gui.text(x+5,185+(450//row_total)*len(master_lst[0][0])+(450//row_total)*len(master_lst[0][1]),
                      'large words','white',10)
    gui.text(1*width+60,145,'Cap/Non-Cap','white',15)
    gui.rectangle(1*width+60,180,125,(450//row_total)*master_lst[1][0],'blue')
    gui.text(1*width+65,185,'Capitalized','white',10)
    gui.rectangle(1*width+60,180+(450//row_total)*master_lst[1][0],125,(450//row_total)
                       *unique_words,'green')
    gui.text(1*width+65,185+(450//row_total)*master_lst[1][0],'Non Capitalized','white',10)
    gui.text(2*width+90,145,'Punct/Non-Punct','white',15)
    gui.rectangle(2*width+90,180,125,(450//row_total)*master_lst[2][0],'blue')
    gui.text(2*width+95,185,'Punctualized','white',10)
    gui.rectangle(2*width+90,180+(450//row_total)*master_lst[2][0],125,(450//row_total)
                        *unique_words,'green')

main()

