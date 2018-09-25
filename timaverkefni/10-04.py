# 10-4

    #             1
    #          1     1
    #        1    2    1
    #      1   3     3   1
    #    1   4    6    4   1
    #  1   5   10   10   5   1

    #     >>> make_new_row([1,1])
    # [1, 2, 1]


# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
