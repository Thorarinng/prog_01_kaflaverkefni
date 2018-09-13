my_word = input("Write a word: ")
print(id(my_word))

for words in my_word:
    print(words, end='')
    print(" ", id(words))