import random 

number = random.randint(1,101)

guess_str = input("Guess a number: ")
guess = int(guess_str)

#while guess is in range
while 0 <= guess <= 100:
		if guess > number:
				print("You guessed to high!")
		elif guess < number:
				print("You guessed to low!")
		else:
				print("You guessed it. Number is: ", number)
				break

		guess_str = input("Guess another number: ")
		guess = int(guess_str)
else:
		print("You quit early. Number was: ", number)
#the end
