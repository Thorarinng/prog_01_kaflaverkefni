# Hlynur Magnus Magnusson 
# hlynurm18@ru.is

tala_1 = int(input("Initial value: "))
tala_2 = int(input("Step: "))

#setja upp breytur
sum = tala_1
sum_of_series = 0

# Lykkju lykur thegar heildarsumman fer upp i eda yfir 100
while sum_of_series <= 100:
    sum_of_series += sum
    print(sum, end=' ')
    # Uppfaeri summu eftir ad buid er ad reikna nyja heildarsummu og birta gildi
    sum += tala_2

print("\nSum of series:", sum_of_series)


# # Hlynur Magnus Magnusson 
# # hlynurm18@ru.is

# tala_1 = int(input("Initial value: "))
# tala_2 = int(input("Step: "))

# #setja upp breytur
# sum = tala_1
# sum_of_series = 0

# # print(sum, end=' ')
# while sum_of_series <= 100:
#     # print(sum, end=' ')
#     # sum += tala_2
#     # print(sum, end=' ')
#     sum_of_series += sum
#     print(sum, end=' ')
#     sum += tala_2

