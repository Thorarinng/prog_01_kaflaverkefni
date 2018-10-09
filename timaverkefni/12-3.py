# 12-3 WORD LIST   Les texta skra. Tekur ut kommur og endurtekningar

import string

#build_wordlist() function goes here
def build_wordlist(wfile):
    """Smidar saman splittadan lista"""
    listi = ''
    for each in wfile:
        removed = remove_punctuation(each)
        listi += removed
    return listi.split()

#remove punctuations
def remove_punctuation(word):
    """Eydir ut punktum og kommum"""
    new_word = ''
    for i in word:
        if i not in string.punctuation:
            new_word += i
            # print(new_word)
    return new_word
          
#find_unique() function goes here
def find_unique(word_list):
    """Finnur hvort listinn endurtekur sig"""
    check_list = []
    for word in word_list:
        if word not in check_list:
            #add word
            check_list.append(word)
    return check_list


def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)
    # print(word_list)

main()