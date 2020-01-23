#
# Author: Adrian Martinez
# Description: Program accepts two inputs from console. I'm bashing my head against my laptop at
# this point. I know what I'm doing wrong but personal family issues are keeping me from thinking
# straight. I'll take the L for this submission.
#

def main():
    word_dic = {}
    suggest_lst = []
    punctuation = [',', '.', '?', '!']
    misspellings = open('misspellings.txt', 'r')
    lines = misspellings.readlines()
    for line in lines:
        add_word(word_dic, line.strip('\n'))
    file_name = input('Enter input file:\n')
    file_txt = open(file_name, 'r')
    file_lst = [line.strip('\n').split(' ') for line in file_txt.readlines()]
    mode = input('Enter spellcheck mode (replace or suggest):\n')
    if mode == 'replace':
        replace(file_lst, word_dic, punctuation)
    if mode == 'suggest':
        suggest(file_lst, suggest_lst, word_dic)

def replace(file_lst, word_dic, punctuation):
    for word in file_lst:
        if word[-1] in punctuation:
            punctuate = word[-1]
            word = word[0:-1]
        if str(word).isupper():
            word = str(word.lower())
            if word in word_dic:
                replace = file_lst.index(word)
                upper_replace = word_dic[word].capitalize()
                file_lst[replace] = str(upper_replace)
    for line in range(len(file_lst)):
        print(str(file_lst))


def suggest(text_lst, suggest_lst, word_dic):
    for i in range(len(text_lst)):
        if str(text_lst[i]).isupper():
            word = text_lst[i].lower()
            if word in word_dic:
                add = text_lst.index(text_lst[i])
                text_lst.insert(add, '('+str(i)+')')
                suggest_lst.append('('+str(i)+')')
                upper_replace = word_dic[word].capitalize()
                suggest_lst.append(upper_replace)
    for line in text_lst:
        print(line)

def add_word(word_dic, line):
    words = line.split(':')
    wrong_key = str(words[-1])
    correct_spell = words[0].split(',')
    if wrong_key not in word_dic:
        word_dic[wrong_key] = str(correct_spell)

main()