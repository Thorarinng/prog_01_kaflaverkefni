top_num = int(input("Input a number between 0 and 999: "))

# power = len(str(top_num))
# a_Numer = 0

# for number in range(int(power)):
#     a_Numer = int(str(top_num)[number])**power
#     print(a_Numer)


# top_num = int(input("Input a number between 0 and 999: "))

# power = len(str(top_num))
# a_Numer = 0
# summa = 0

# for number in range(int(power)):
#     a_Numer = int(str(top_num)[number])**power
#     print(a_Numer)
#     summa += a_Numer
# print(summa)


for num in range(top_num):

    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp%10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)