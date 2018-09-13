grade = float(input("Input a grade: ")) # Do not change this line

# Fill in the missing code below
if grade < 0.0 or grade > 10.0:
    print("Invalid grade!") # Do not change this line
elif 5.0 <= grade <= 10.0:
    print("Passing grade!") # Do not change this line
else:
    print("Failing grade!") # Do not change this line