n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
divider = 2
prime = True
while (divider < n):
    if n%divider == 0:
        prime = False
    divider += 1

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")