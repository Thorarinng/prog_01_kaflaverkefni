# Your function definition goes here
def count_case(strengur):
    """Tekur inn streng og telur: return upper, lower"""
    upCount = 0
    lowCount = 0

    for stafur in strengur:
        if stafur.isupper():
            upCount += 1
        elif stafur.islower():
            lowCount += 1

    return upCount, lowCount

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)