n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
divider = 1
while divider <= n:
    if n%divider == 0:
        print(divider)
    divider += 1