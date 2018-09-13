#!/usr/bin/python3.7

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

maxNum = 0

if (num1 > num2) and (num1 > num3):
	maxNum = num1
elif num3 > num2:
	maxNum = num3
else:
	maxNum = num2

print("Max number is: ", maxNum)
