# Hlynur Magnus Magnusson
# hlynurm18@ru.is
# Skilaverkefni 04; Stock Price

    # Enter number of shares: 100
    # Enter price (dollars, numerator, denominator): 29 a b
    # Invalid price!
    # Enter price (dollars, numerator, denominator): 29 7 8
    # 100 shares with market price 29 7/8 have value $2987.50
    # Continue: y
    # Enter number of shares: 1a
    # Invalid number!
    # Enter number of shares: 30
    # Enter price (dollars, numerator, denominator): x 1 2
    # Invalid price!
    # Enter price (dollars, numerator, denominator): 89 1 2
    # 30 shares with market price 89 1/2 have value $2685.00
    # Continue: n


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
            break
        except ValueError:
            print("Invalid price!")
    return dollars, numerator, denominator


# Call for shares
my_shares = ask_for_shares()
dollars, numerator, denominator = enter_price()

print("Shares:", my_shares)
print("Dollars:", dollars, "Numerator:", numerator, "Denominator:", denominator)