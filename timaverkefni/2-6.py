d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below
if (1 <= d1 <= 6) and (1 <= d2 <= 6):
    sum = d1 + d2
    if sum == 7 or sum == 11:
        print("Winner")
    elif sum == 2 or sum == 3 or sum == 12:
        print("Loser")
    else:
        print(sum)
else:
    print("Invalid input")
