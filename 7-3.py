# The function definition goes here
def range_test(tala):
    if 1 < tala < 555:
        print(tala, "is in range.") 
        return True
    else:
        print(tala, "is outside the range!")
        return False

num = int(input("Enter a number: "))

# You call the function here
range_test(num)