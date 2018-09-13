# Hlynur Magnus

# get integer number from input
# max_int starts out as first number
# check if number is negative
# if number is negative exit loop
# while the number is positive
# ask for a new number
# check if new number is bigger than old number (max_int)
# if number is bigger then make new number max_int
# when input is negative the loop stops

# after loop is stopped print current max_int number


num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line


