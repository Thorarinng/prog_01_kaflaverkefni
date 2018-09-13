#!/usr/bin/python3.7

six_digits = int(input("Gimme them damn 6 digits: "))

first_three = six_digits//1000
last_two = six_digits%100
middle_two = (six_digits%10000)//100

print("First three: {}, last two: {}, middle two: {}".format(first_three, last_two, middle_two))
