#!/usr/bin/python3.6

squares = 64
sum = 0

for i in range(64):
	print("Grains on", i+1, "are", 2**i)
	sum += (2**i)
	print(sum)
print("final sum: ", sum)


