# is_prime function definition goes here
def is_prime(tala):
    if tala > 1:
        for i in range(2,tala):
            if tala%i == 0:
                return (print(tala, "is not a prime"))
        return (print(tala, "is a prime"))

# def is_prime(tala):
#     """Finnur ef tala er prime: tala"""
#     divider = 2
#     while (divider < tala):
#         if tala%divider == 0:
#             return (print(tala, "is not a prime"))
#         divider += 1
#     return (print(tala, "is a prime"))

    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
is_prime(num)