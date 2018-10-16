# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Project 7 - Tic Tac Toe
import string


def make_grid(m_size):
    """Takes size input m and creates a grid of m * m size"""
    # initialize an empty grid
    matrix_grid = []
    count = 1

    for row in range(m_size):
        temp_list = []
        for col in range(m_size):
            temp_list.append(count)
            count += 1
        matrix_grid.append(temp_list)
    # returns the nested matrix populated
    return matrix_grid


def Error_Illegal():
    print("Illegal move!")


def Error_WrongSize():
    print("Write an integer 3 or above.")


def player_input(player, m_size, m_grid):
    """ Asks for valid input within matrix space
        and if it's valid then returns the number"""
    choice = True
    grid_size = m_size*m_size
    while choice:
        try:
            player_move = int(input("{} position: ".format(player)))
            row, col = find_position(m_size, player_move)
            # if move legal and inside boundaries then move on
            if 1 <= player_move <= grid_size and legal_move(row, col, m_grid):
                update_matrix(row, col, m_grid, player)
                choice = False
            else:
                Error_Illegal()
        # if not integer
        except ValueError:
            Error_Illegal()
    return player, row, col


def legal_move(x_pos, y_pos, m_grid):
    """Is there an X or O in that spot"""
    is_legit = True
    letters = 'XO'
    pos_value = m_grid[x_pos][y_pos]
    if str(pos_value) in letters:
        is_legit = False
    return is_legit


def print_matrix(m_size, m_grid):
    """Prints out a nice matrix in nice rows and columns independent of size"""
    for row in range(m_size):
        for col in range(m_size):
            value = m_grid[row][col]
            print("{:>5}".format(value), end="")
        print("")


def player_switcher(player):
    """Switch player"""
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    return player


def find_position(size, grid_num):
    """Find position based on matrix size and location number"""
    x_pos = (grid_num-1) // (size)
    y_pos = (grid_num-1) % size
    return x_pos, y_pos


def is_full(m_size, m_grid):
    """Takes in the matrix and returns updated with latest move"""
    is_full = True
    # is the board full
    for row in range(m_size):
        for col in range(m_size):
            if str(m_grid[row][col]).isnumeric():
                is_full = False
    return is_full


def win_check(m_size, m_grid, row, col):
    win = False
    if check_rows(m_size, m_grid, row):
        win = True
    elif check_columns(m_size, m_grid, col):
        win = True
    elif check_angle_right(m_size, m_grid):
        win = True
    elif check_angle_left(m_size, m_grid):
        win = True
    return win


def check_rows(m_size, m_grid, row):
    """check all rows for a match"""
    i_win = False
    x_count = 0
    o_count = 0
    for col in range(m_size):
        if m_grid[row][col] == 'X':
            x_count += 1
        elif m_grid[row][col] == 'O':
            o_count += 1
    if x_count == m_size or o_count == m_size:
        i_win = True
    return i_win

def check_columns(m_size, m_grid, col):
    """check all columns for a match"""
    i_win = False
    x_count = 0
    o_count = 0
    for row in range(m_size):
        if m_grid[row][col] == 'X':
            x_count += 1
        elif m_grid[row][col] == 'O':
            o_count += 1
    if x_count == m_size or o_count == m_size:
        i_win = True
    return i_win

def check_angle_right(m_size, m_grid):
    """Check if there are a match diagonally"""
    i_win = False
    x_count = 0
    o_count = 0
    for row in range(m_size):
        if m_grid[row][row] == 'X':
            x_count += 1
        elif m_grid[row][row] == 'O':
            o_count += 1
    if x_count == m_size or o_count == m_size:
        i_win = True
    return i_win

def check_angle_left(m_size, m_grid):
    """Check if there are a match diagonally"""
    i_win = False
    x_count = 0
    o_count = 0
    for row in range(m_size):
        col_pos = (m_size-1)-row
        if m_grid[row][col_pos] == 'X':
            x_count += 1
        elif m_grid[row][col_pos] == 'O':
            o_count += 1
    if x_count == m_size or o_count == m_size:
        i_win = True
    return i_win

def update_matrix(row, col, m_grid, player_letter):
    """Get position and update matrix"""
    check_val = m_grid[row][col]
    m_grid[row][col] = player_letter


def Ask_Size():
    wrong_num = True
    while wrong_num:
        matrix_size = int(input("Input dimension of the board: "))
        try:
            matrix_size = int(matrix_size)
            if matrix_size >= 3:
                wrong_num = False
            else:
                Error_WrongSize()
        except ValueError:
            Error_WrongSize()
    return matrix_size


def print_win(player):
    print("Winner is: {}".format(player))


def game_loop(matrix_size, matrix):
    # Starting player
    player = 'X'
    game_on = True

    while game_on:

        # print out new matrix
        print_matrix(matrix_size, matrix)

        if not is_full(matrix_size, matrix):
            # take input and return a valid move
            player, row, col = player_input(player, matrix_size, matrix)

        # Check win status
        am_i_full = is_full(matrix_size, matrix)
        if not win_check(matrix_size, matrix, row, col) and not am_i_full:
            game_on = True
            player = player_switcher(player)
        elif am_i_full:
            print("Draw!")
            game_on = False
        else:
            print_win(player)
            game_on = False


def main():
    matrix_size = Ask_Size()
    matrix = make_grid(matrix_size)
    game_loop(matrix_size, matrix)   # put the main loop into a game loop


# Run the main loop
main()
