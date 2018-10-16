# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Project 7 - Tic Tac Toe

# 1 ask_size
# 2 make_grid
# 3 ask_player ? input
# 4 update_grid
#     -if illegal move let know
#     -if legal finish update grid
#     -switch player
#     -check winning state
            # -is there m_size symbols in a row
            # -is the board filled
# 5 ask_player ? input


def make_grid(m_size):
    """Takes size input m and creates a grid of m * m size"""

    #initialize an empty grid
    matrix_grid = []
    count = 1

    for row in range(m_size):
        temp_list = []
        for col in range (m_size):
            temp_list.append(count)
            count += 1
        matrix_grid.append(temp_list)
    #returns the nested matrix populated
    return matrix_grid

def player_input(player, m_size, m_grid):
    """ Asks for valid input within matrix space
        and if it's valid then returns the number"""
    choice = True
    grid_size = m_size*m_size

    while choice:
        try:
            player_move = int(input("{} position: ".format(player)))
            if 1 <= player_move <= grid_size:
                # if check_board(player_move, m_grid )== True:
                choice = False
            else:
                print("Illegal move!")
        except ValueError:
            print("Illegal move!")
    # Returns a legal move based on type and  grid size        
    return player, player_move

def print_matrix(m_size, m_grid):
    """Prints out a nice matrix in nice rows and columns"""
    for row in range(m_size):
        for col in range(m_size):
            value = m_grid[row][col]
            print("{:>5}".format(value), end="")
        print("")


def player_switcher(player):
    """Switch player"""
    if player == 'X':
        player = 'O'
    else:
        player == 'X'
    return player



def update_matrix(m_grid):
    """Takes in the matrix and returns updated with latest move"""

    #update matrix if number is not already in the same place with X or O
    matrix_grid =  m_grid
    return matrix_grid






# def check_board(p_move, m_grid):
#     """ Check if the move is possible in the board returns true or false"""
#     for row in range(len(m_grid)):
#         for col in range(len(m_grid)):
#             if p_move == m_grid[row][col]:
#                 print(row+1, col+1)
#                 print("Move is legit!")
#                 return True
#     print("False move yoh!")
#     return False


def board_loop(p_move, player_symbol, m_grid):
    """Runs through board with a check"""
    legal_move = False
    for row in range(len(m_grid)):
        for col in range(len(m_grid)):
            if m_grid[row][col] == p_move:
                legal_move = True
                m_grid[row][col] = player_symbol
    return legal_move
# def game_loop():

    #what player is currently playing


    #mark that players move

    #check if the move worked

    #update to next player
# player = 'X'

def main():
    player = 'X'
    # matrix size >= 3
    # matrix_size = int(input("Input dimension of the board: "))
    matrix_size = 4
    matrix = make_grid(matrix_size)

    # game_loop()   # put the main loop into a game loop
    print_matrix(matrix_size ,matrix)
    player, p_move = player_input(player, matrix_size, matrix)
    print("player input is:", p_move, " player is ", player)
    player = player_switcher(player)
    print("new player is {}!".format(player))

main()