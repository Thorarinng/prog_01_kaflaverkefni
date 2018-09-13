top_num = int(input("Upper number for the range: ")) # Do not change this line

# pNum = 0

# for i in range(1, top_num):
#     if top_num%i==0:
#         pNum += i
#         print(i)
# print(pNum)

for c in range (1, top_num):
    if sum(x for x in range(1,c) if not c % x) == c:
        print(c)