# Hlynur Magnus Magnusson
# hlynurm18@ru.is
# Skilaverkefni 04; Stock Price

# Fastar og breytur
answer = 'y'

def ask_for_shares():
    """Asks for shares until it gets a valid number"""
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            break
        except ValueError:
            print("Invalid number!")
            continue
    return shares

def enter_price():
    """Asks for price: Wants price in; dollars, numerator, denominator"""
    while True:
        try:
            dollars, numerator, denominator = input("Enter price (dollars, numerator, denominator): ").split()
            dollars = int(dollars)
            numerator = int(numerator)
            denominator = int(denominator)
            # check if denominator > 0 and raise except if not
            break
        except ValueError:
            print("Invalid price!")
    return dollars, numerator, denominator

def the_stock_value(shares, dollars, numerator, denominator):
    """Calculates and prints out the value of the stocks"""
    stock_value = (shares * (dollars + numerator/denominator))

    print("{} shares with market price {} {}/{} have value ${:.2f}".format(shares, dollars, numerator, denominator, stock_value))

# Start program
while answer == 'y' or answer == 'yes':
    # Call for shares
    my_shares = ask_for_shares()
    dollars, numerator, denominator = enter_price()
    the_stock_value(my_shares, dollars, numerator, denominator)

    answer = input("Continue: ").lower()