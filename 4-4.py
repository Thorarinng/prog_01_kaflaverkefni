m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m > n:
    bigger_num = m
else:
    bigger_num = n

for i in range(2, bigger_num+1):
    if m%i==0 and n%i==0:
        GCD = i
print(GCD)