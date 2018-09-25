# 10-1

import string

sentence = input("Input a sentence: ")

# Here you should add the missing part
unique_letters = []

for char in sentence:
    # if char.isalpha() and char not in unique_letters:
    #     unique_letters.append(char)
    if char not in string.punctuation and char not in string.whitespace:
        if char not in unique_letters:
            unique_letters.append(char)


print("Unique letters:", unique_letters)
