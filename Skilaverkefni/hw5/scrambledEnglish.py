# Hlynur Magnus Magnusson
# hlynurm18@ru.is
# Skilaverkefni 05; Scrambled English

import random
import string

def get_word_string(fname):
    """Naer i skra sem spurt er um"""

    #nyr tomur strengur
    new_string = ''

    try:
        with open(fname, 'r',) as rfile:
            for line in rfile:
                new_string += line

    # Calls error and halts the program if file not found
    except FileNotFoundError:
        print("File {} not found".format(fname), end='')

    return new_string.split()


def randomize_string(rand_string):
    """takes strings and scrambles the middle of them"""
    if len(rand_string) <= 3:
        return rand_string
        #don't bother with short rand_strings
    punctuation = ',.:;-'
    if punctuation in rand_string:
         #take first and last, as well as the punctuation
        first, mid, end = rand_string[0], rand_string[1:-1], rand_string[-2]
    else:
        #take first and last letter from word
        first, mid, end = rand_string[0], rand_string[1:-1], rand_string[-1]
    
    chars = list(mid); random.shuffle(chars)
        #randomize mid section of word

    #merge word back together
    mid = ''.join(chars)
    
    return first+mid+end

def scramble_string(wstring):
    """Ruglar i strengnum"""

    #nyr tomur strengur
    new_string = ""
    wspace = ' '

    for each in wstring:
        if len(each) > 3:
            new_string += randomize_string(each) + wspace # randomize_string(each)
        else:
            new_string += each + wspace
    return new_string
    

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)