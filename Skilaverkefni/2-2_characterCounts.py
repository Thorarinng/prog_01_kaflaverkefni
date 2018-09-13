# Hlynur Magnus Magnusson
# Hlynurm18@ru.is

import string

my_string = input("Enter a sentence: ")

count_digit = 0
count_lower = 0
count_upper = 0
count_punktur = 0

# for every character in the string it checks for digits, lower, upper and punctuations
# on each encounter we add one to the counter
for char in my_string:
    if char.isdigit():
        count_digit += 1
    elif char.islower():
        count_lower += 1
    elif char.isupper():
        count_upper += 1
    elif char in string.punctuation:
        count_punktur += 1

print("{:>15}{:>6}".format("Upper case", count_upper))
print("{:>15}{:>6}".format("Lower case", count_lower))
print("{:>15}{:>6}".format("Digits", count_digit))
print("{:>15}{:>6}".format("Punctuation", count_punktur))


