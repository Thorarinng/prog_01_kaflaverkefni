#Find the perfect number
top_num_str = input("What is the upper number? ")
top_num = int(top_num_str)
number = 2
while number <= top_num:
		#sum up the divisors
		divisor = 1
		sum_of_divisors = 0
		while divisor < number:
				if number % divisor == 0:
						sum_of_divisors += divisor
				divisor += 1

		#classify the number based on it's divisor sum
		if number == sum_of_divisors:
				print(number, "is perfect")
		if number < sum_of_divisors:
				print(number, "is abundant")
		if number > sum_of_divisors:
				print(number, "is deficient")
		number += 1
