nums = [1,2,3]

for num in nums:
    if num == 3:
        print('Found:', num)
        continue
        # break
    print(num)


#first loop
for num in nums:
    #second loop
    for letter in 'Hallo':
        print(num, letter + " blurb")

for num in range(2,11,2):
    print(num)