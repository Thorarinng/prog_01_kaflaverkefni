# 10-4

def make_new_row(row):
    length=len(row)
    row.append([])
    row[i].append(1)
    for j in range(1,i):
        row[i].append(row[i-1][j-1]+row[i-1][j])
    if(length!=0):
        row[i].append(1)
    print(row[-1])
    return row
# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)


#     #             1
#     #          1     1
#     #        1    2    1
#     #      1   3     3   1
#     #    1   4    6    4   1
#     #  1   5   10   10   5   1

#     #     >>> make_new_row([1,1])
#     # [1, 2, 1]

# # n=int(input("Enter number of rows: "))
# # a=[]
# # for i in range(n):
# #     a.append([])
# #     a[i].append(1)
# #     for j in range(1,i):
# #         a[i].append(a[i-1][j-1]+a[i-1][j])
# #     if(n!=0):
# #         a[i].append(1)
# # for i in range(n):
# #     print("   "*(n-i),end=" ",sep=" ")
# #     for j in range(0,i+1):
# #         print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
# #     print()

# def make_new_row(new_row):
#     for i in range(height):
#         new_row.append([])
#         new_row[i].append(1)
#         for j in range(1,i):
#             new_row[i].append(new_row[i-1][j-1]+new_row[i-1][j])
#         if(height!=0):
#             new_row[i].append(1)
#         print(new_row)
#         return new_row
#     # for i in range(height):
#     #     print("   "*(height-i),end=" ",sep=" ")
#     #     for j in range(0,i+1):
#     #         print('{0:6}'.format(new_row[i][j]),end=" ",sep=" ")
#     #     print()


# # Main program starts here - DO NOT CHANGE
# height = int(input("Height of Pascal's triangle (n>=1): "))
# new_row = []
# for i in range(height):
#     new_row = make_new_row(new_row)
#     # print(new_row)
