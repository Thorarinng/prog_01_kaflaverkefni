# find_min function definition goes here
def find_min(num1,num2):
    if num1 < num2:
        minimum = num1
    else:
        minimum = num2
    return minimum


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)

print("Minimum: ", minimum)