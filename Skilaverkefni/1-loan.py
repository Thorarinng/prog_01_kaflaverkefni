# Hlynur Magnus Magnusson
# hlynurm18@ru.is
# Skilaverkefni 01; Forritun

loan = int(input("Input the cost of the item in $: "))

#byrjunar fastar
month = 0
montly_minimum = 50.0
total_interest_paid = 0.0

# Vaxta breytir á láni
if loan <= 1000:
    interest = 0.015
else:
    interest = 0.02

# Reikna borgunar lúppu
while loan > 0.0:

    month += 1

    # Umreikna vexti mánaðarlega
    interest_paid = loan * interest

    # Athuga hvort minna sé eftir af láni heldur en föst mánaðargreiðsla
    if montly_minimum < loan:
        montly_minimum = 50.0
    else:
        montly_minimum = loan + interest_paid



    loan = (loan + interest_paid) - montly_minimum

    print(  "Month:", month, \
            "Payment:", round(montly_minimum, 2), \
            "Interest paid:", round(interest_paid, 2), \
            "Remaining debt:", round(loan, 2))

    total_interest_paid += interest_paid
    

print("")
print("Number of months: ", month)
print("Total interest paid: ", round(total_interest_paid,2))
