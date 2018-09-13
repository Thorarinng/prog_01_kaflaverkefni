# for i in range(1,11):
#     base = i
#     for k in range(1,11):
#         multi = base * k
#         print("{:>5}".format(multi), end='')
#     print("")

# Tvofold lykkja med base og step
for base in range(1,11):
    for step in range(1,11):
        multiplication = base * step
        #setur upp formatid a utkomunni
        print("{:>5}".format(multiplication), end='')
    #tryggir ad ny lina kemur i lok lykkju
    print("")