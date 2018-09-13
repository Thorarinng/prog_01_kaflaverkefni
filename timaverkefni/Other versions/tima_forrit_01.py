num_int = int(input("Upper number for the range: "))

products = 0
for number in range(1, num_int):
    products - products * number

print(products)