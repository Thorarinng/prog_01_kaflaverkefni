# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Project 3 - Moving a Character

# FASTAR
LEFT_EDGE = 1
RIGHT_EDGE = 10

LEFT_KEY = 'l'
RIGHT_KEY = 'r'

# UPPHAFS GILDI
letter = 'r'    # athuga hvort thetta thurfi
vera_loc = 5    # athuga hvort thetta thurfi


# FUNCTIONS ========================================================

def start_point():
    """Asks for the start point """
    point = int(input("Input a position between 1 and 10: "))
    return point

def new_key(vera_loc):      # breyting
    """Questions and directives"""
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    letter = input("Input your choice: ")
    print("New position is: ", vera_loc)
    return letter

def mover(the_key, new_loc):
    # new_loc = vera_loc
    if (new_loc > LEFT_EDGE) and (the_key == LEFT_KEY):
        new_loc -= 1 
    elif (new_loc < RIGHT_EDGE) and (the_key == RIGHT_KEY):
        new_loc += 1
    return new_loc

def start(the_location):
    """Keyrir saman follin, tekur inn upphafs stadsetningu"""
    
    # Upphafs gildi
    vera_loc = the_location         # breyting
    my_key = new_key(vera_loc)      # breyting
    # vera_loc = the_location

    # Keyra game loop
    while (my_key == LEFT_KEY) or (my_key == RIGHT_KEY):
        vera_loc = mover(my_key, vera_loc)
        # print("New position is: ", vera_loc)  # breyting
        my_key = new_key(vera_loc)  # breyting
        # print("New position is: ", vera_loc)  # breyting

# FUNCTIONS ENDIR ==================================================


# Byrjun a keyrslu
s_point = start_point()

# Ef upphafs punktur er innan settra marka
if 1 <= s_point <= 10:
    start(s_point)



# Input a position between 1 and 10: 7
# l - for moving left
# r - for moving right
# Any other letter for quitting
# Input your choice: r
# New position is: 8
# l - for moving left
# r - for moving right
# Any other letter for quitting
# Input your choice: r
# New position is: 9
# l - for moving left
# r - for moving right
# Any other letter for quitting
# Input your choice: r
# New position is: 10