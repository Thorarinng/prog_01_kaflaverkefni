percent_float = float(input("Your percentage? "))

if 90 <= percent_float < 100:
	print("You get: A")
elif 80 <= percent_float < 90:
	print("You get: B") 
elif 70 <= percent_float < 80:
	print("You get: C")
elif 60 <= percent_float < 70:
	print("You get: D")
else:
	print("oops you fail!")
