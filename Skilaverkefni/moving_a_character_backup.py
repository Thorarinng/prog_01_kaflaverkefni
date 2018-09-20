# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Project 3 - Moving a Character

# FASTAR
LEFT_EDGE = 1
RIGHT_EDGE = 10

LEFT_KEY = 'l'
RIGHT_KEY = 'r'

# UPPHAFS GILDI
letter = 'r'
vera_loc = 5


# FUNCTIONS ========================================================

def start_point():
    """Asks for the start point """
    point = int(input("Input a position between 1 and 10: "))
    return point

def new_key():
    """Questions and directives"""
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    letter = input("Input your choice: ")
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
    my_key = new_key()
    vera_loc = the_location

    # print("The new key is: ", my_key)
    # print("Start location is: ", vera_loc)

    while (my_key == LEFT_KEY) or (my_key == RIGHT_KEY):
        vera_loc = mover(my_key, vera_loc)
        print("New position is: ", vera_loc)
        my_key = new_key()

# FUNCTIONS ENDIR ==================================================

# Byrjun a keyrslu
s_point = start_point()

if 1 <= s_point <= 10:
    # vera_loc = s_point
    # print("I upphafi er vera loc: ", vera_loc)
    start(s_point)

