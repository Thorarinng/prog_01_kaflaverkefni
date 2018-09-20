# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Project 3 - Moving a Character

# FASTAR
LEFT_EDGE = 1
RIGHT_EDGE = 10

LEFT_KEY = 'l'      # key input setup
RIGHT_KEY = 'r'     # key input setup

# FUNCTIONS ========================================================

def start_point():
    """Asks for the start point """
    point = int(input("Input a position between 1 and 10: "))
    return point

def start(the_location):
    """Keyrir saman follin, tekur inn upphafs staðsetningu"""
    # Initialize upphafs gildi
    my_key = new_key()
    location = the_location

    # Keyra game loop
    while (my_key == LEFT_KEY) or (my_key == RIGHT_KEY):
        location = mover(my_key, location)
        update_location(location)
        my_key = new_key()

    update_location(location)

def new_key():
    """Questions and directives; returns input letter"""
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    letter = input("Input your choice: ")
    return letter

def mover(the_key, new_loc):
    """Checks boundaries and updates the location to new location"""
    if (new_loc > LEFT_EDGE) and (the_key == LEFT_KEY):
        new_loc -= 1 
    elif (new_loc < RIGHT_EDGE) and (the_key == RIGHT_KEY):
        new_loc += 1
    return new_loc

def update_location(current_position):
    """Prints out current location; input: location"""
    print("New position is:", current_position)

# FUNCTIONS ENDIR ==================================================


# Byrjar a ad finna upphafs punkt
s_point = start_point()

# Ef upphafs punktur er innan settra marka
if 1 <= s_point <= 10:
    start(s_point)