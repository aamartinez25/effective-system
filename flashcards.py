import random

def main():
    words = []
    definitions = []
    card_num = int(input('Enter number of flashcards to create: '))
    get_card(words, definitions, card_num)
    quiz(words, definitions)

def get_card(words, definitions, card_num):
    i = 0
    while i < card_num:
        word_input = input('Enter word: ')
        word_def = input('Enter word definition: ')
        words.append(word_input)
        definitions.append(word_def)
        i += 1

def word_card(content):
    print('+--' + ('-' * len(content)) + '--+')
    print('|  ' + content + '  |')
    print('+--' + ('-' * len(content)) + '--+')

def quiz(words, definitions):
    i = 0
    while i < len(words):
        random_position = random.randint(0, len(words) -1)
        def_position = definitions[random_position]
        content = words[random_position]
        word_card(content)
        input('press enter to continue')
        content = definitions[def_position]
        word_card(content)
        input('press enter to continue')
    i += 1

main()