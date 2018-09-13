# Hlynur Magnus Magnusson
# Hlynurm18@ru.is

my_string = input("Enter a word: ")
my_string = my_string.lower()

# While string is not empty the loop keeps going
while (my_string and (my_string != ".")):

    # Collection of vowels
    vowels = 'aeiouy'
    suffix = 'ay'

    # This pig latin formula works for all word not starting with a vowel
    for index, my_char in enumerate(my_string):
        if my_char in vowels:
            # Check if first my_char is a vowel and change suffix accordingly
            if index == 0:
                suffix = 'yay'
            # If index 0 is vowel then break  
            break
    
    # Edge case if no vowels are in the word
    if index == len(my_string)-1:
        index = 0
            
    # Print the pig latin split up word with correct ending
    print("{}{}{}".format(my_string[index:], my_string[:index], suffix))
    my_string = input("Enter a word: ")