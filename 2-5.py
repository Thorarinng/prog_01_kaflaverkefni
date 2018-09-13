
# yes=True

# while(yes):
year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(True)
# else:
#     print(False)

    # if year%4 == 0:
    #     if year%100 != 0 or year%400 == 0:
    #         print(True)
    #     else:
    #         print(False)

# answer = input("Wanna keep askin? (y or n)")
# if answer == 'y':
#     yes = True
# else:
#     yes = False


# Fill in the missing code below
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(True)
else:
    print(False)