# 10-3 Triple string print

# Your functions should appear here
def populate_list(strengur):
    """"""
    while True:
        svar = input("Enter value to be added to list: ")
        if svar.lower() != 'exit':
            strengur.append(svar)
        else:
            break
    return strengur

def triple_list(strengur):
    return strengur * 3


# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
