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

    # punctuation = '.,;:'
    first, center, last = '', '', ''

    for char in rand_string:
        if char in string.punctuation:
            print("there!", rand_string)
            first, center, last = rand_string[0], rand_string[1:-2], rand_string[-1]
            # return rand_string
        else:
            return rand_string
        # return rand_string + "skunkurrrr "
        # return center

    # if punctuation in rand_string:
    #     return rand_string[:-1] + "fuuuuuuck "

    # for i in range(len(rand_string)):
    #     if rand_string[i] in string.punctuation:
    return center


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

# def word_randomize(word):
#     if len(word) <= 3:
#         return word
#         #don't bother with short words
#     punctuation = ',.:;-'
#     if punctuation in word:
#         first, mid, end = word[0], word[1:-1], word[-2]
#         #take first and last, as well as the punctuation
#     else:
#         first, mid, end = word[0], word[1:-1], word[-1]
#         #take first and last letter from word
    
#     chars = list(mid); random.shuffle(chars)
#         #randomize mid section of word

#     mid = ''.join(chars)
#         #merge word back together
    
#     return first+mid+end


# def scramble_string(word_string):
#     list_of_words, randomized_string, i = word_string, '', 0 
#     #just for clarity, rename the list "list of words"
#     #sloppy way to send each word to randomize
    
#     while i < len(list_of_words):
#         word = list_of_words[i]
#         word_randomize(word)
#         i += 1 
#         randomized_string += (word_randomize(word) + ' ')
#         # send each word to randomize function
#         # convert list back to string

#     return randomized_string 

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)