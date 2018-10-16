def full(size, listi):
    is_full = True
    for x in range(size):
        for y in range(size):
            if str(m_grid[x][y]).isnumeric():
                is_full = False
    return is_full


4     5     6  
7     8     9
4     5     6 
7     8     9
4     5     6 
7     8     9