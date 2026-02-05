def _decode_thermometers_string( task:str ) -> tuple[int,list[int],list[int],list[list[int]]]:
    """
    Decodes the given Thermometers instance.

    Arg
    ---
    task: str
        A Thermometers instance encoded as a string

    Returns
    -------
    n: int
        Size of the grid, i.e., the number of rows (= number of columns).
    colnums: list[int]
        List of the side numbers for columns (left to right).
    rownums: list[int]
        List of the side numbers for rows (up to bottom).
    thermometers: list[list[int]]
        List of the thermometers, where each thermometer is a list of numbers referring to the covered cells.
    """
    split = task.split( ';' )
    numbers = list( map( int, split[0].split( '_' ) ) )

    n = len(numbers) // 2
    colnums = numbers[:n]
    rownums = numbers[n:]
    thermometers = []
    grid = [ None for _ in range(n*n) ] # temporary list to maintain empty/filled cells

    for tm in split[1:]:
        tms = list( map( int, tm.split( ',' ) ) )

        start = grid.index( None ) # first empty cell

        if tms[0] == 1: # left -> right
            thermometers.append( [ start + i for i in range(tms[1]) ] )
        elif tms[0] == 2: # right -> left
            thermometers.append( [ start + tms[1] - 1 - i for i in range(tms[1]) ] )
        elif tms[0] == 3: # top -> bottom
            thermometers.append( [ start + i*n for i in range(tms[1]) ] )
        elif tms[0] == 4: # bottom -> top
            thermometers.append( [ start + (tms[1]-1)*n - i*n for i in range(tms[1]) ] )
        elif tms[0] == 5: # custom
            thermometers.append( tms[1:] )
        else:
            raise ValueError( f'unexpected type of thermometer: {tms[0]}' )

        for i in thermometers[-1]:
            grid[i] = len(thermometers)

    return n, colnums, rownums, thermometers

def _encode_thermometers_cells( cells:list[int] ) -> str:
    """
    Encodes the given list of cells in a string.
    
    Args
    ----
    cells: list[int]
        The solution, i.e., the list of cells filled with mercury.

    Returns
    -------
    : str
        The solution encoded as a string.
    """
    return ','.join( map( str, sorted(cells) ) )

def _print_thermometers( n:int, colnums:list[int], rownums:list[int], thermometers:list[list[int]], solution:list[int]= None ) -> None:
    """
    Prints the given Thermometers instance/solution

    Args
    ---
    n: int
        Size of the grid, i.e., the number of rows (= number of columns).
    colnums: list[int]
        List of the side numbers for columns (left to right).
    rownums: list[int]
        List of the side numbers for rows (up to bottom).
    thermometers: list[list[int]]
        List of the thermometers, where each thermometer is a list of numbers referring to the covered cells.
    solution: list[int]
        Solution (optional).
    """
    CHARS = ' ╶╵└╴─┘┴╷┌│├┐┬┤┼'
    
    table = [ 0 for _ in range(n**2) ]

    for tm in thermometers:            
        for i in range(1,len(tm)):
            if tm[i-1] + 1 == tm[i]: # left -> right
                table[tm[i-1]] += 1
                table[tm[i]]   += 4
            elif tm[i-1] - 1 == tm[i]: # right -> left
                table[tm[i-1]] += 4
                table[tm[i]]   += 1
            elif tm[i-1] + n == tm[i]: # top -> bottom
                table[tm[i-1]] += 8
                table[tm[i]]   += 2
            elif tm[i-1] - n == tm[i]: # bottom -> top
                table[tm[i-1]] += 2
                table[tm[i]]   += 8

    table = list( map( lambda type: CHARS[type], table ) )

    if solution != None:
        for cell in range(len(table)):
            if cell not in solution:
                table[cell] = ' '

    header0 = list( map( lambda num: str(num % 10), colnums ) )
    header1 = list( map( lambda num: str(num // 10) if 10 <= num else ' ', colnums ) )

    print( '  ', ''.join( header1 ) )
    print( '  ', ''.join( header0 ) )
    for i in range(n):
        print( f'{rownums[i]:2d}', ''.join( table[i*n:(i+1)*n] ) )

def _solve_thermometers( n:int, colnums:list[int], rownums:list[int], thermometers:list[list[int]] ) -> list[int]:
    """
    Solves the given Thermometers instance.

    Args
    ----
    n: int
        Size of the grid, i.e., the number of rows (= number of columns).
    colnums: list[int]
        List of the side numbers for columns (left to right).
    rownums: list[int]
        List of the side numbers for rows (up to bottom).
    thermometers: list[list[int]]
        List of the thermometers, where each thermometer is a list of numbers referring to the covered cells.

    Returns
    -------
    : list[int]
        Solution: list of the cells filled with mercury.
    """
    print('!!! TODO: implement Thermometers solver !!!')

    return [ i*n+j for i in range(n) for j in range(n) ]

def solve_thermometers( task:str, print_task:bool= False, print_solution:bool= False ) -> list[int]:
    """
    Solves the given Thermometers instance.    

    Args
    ----
    task: str
        A Thermometers instance encoded as a string
    print_task: bool
        Should we print the task?
    print_solution: bool
        Should we print the solution?

    Returns
    -------
    : list[int]
        The list of the cells filled with mercury encoded as a string
    """
    # decode (and print) task
    n, colnums, rownums, thermometers = _decode_thermometers_string( task )
    if print_task:
        _print_thermometers( n, colnums, rownums, thermometers, solution= None )

    # solve (and print) task
    solution = _solve_thermometers( n, colnums, rownums, thermometers )
    if print_solution:
        _print_thermometers( n, colnums, rownums, thermometers, solution= solution )

    return _encode_thermometers_cells( solution )

if __name__ == '__main__':    
    TASKS = [
        '1_1_2_3_1_1_2_3;3,3;3,2;3,2;3,3;1,2;1,2;1,2',
        '3_2_1_1_2_1_2_2;1,2;5,2,3,7;5,4,8,12,13,14,15;5,9,5,6;1,2',
        '4_1_2_2_4_4_4_3_1_2_4_3;1,3;1,3;4,5;1,2;1,3;4,3;3,2;1,2;4,2;2,2;2,2;1,2;2,5',
        '4_3_4_2_1_3_2_2_2_4_2_5;2,2;5,2,3,4,10,9;4,4;2,2;5,8,14,20,26,27,28,29;5,18,12,13,19;5,21,15,16,22;3,2;5,25,31,32,33,34,35',
        '7_5_3_5_4_7_4_4_5_5_6_6_7_3_3_6_4_8_3_3;4,2;2,5;4,2;3,3;3,5;3,3;3,3;3,9;3,3;3,3;4,4;3,7;3,8;4,2;4,2;4,5;2,2;3,4;4,2;3,5;1,2;4,3;3,2;4,2;4,2;1,3;1,2;1,2;2,3',
        '7_4_3_7_6_6_7_3_1_5_2_7_8_9_4_4_3_5_5_2;5,60,50,40,30,20,10,0,1,11;4,2;5,35,25,15,14,13,3,4;5,26,16,6,5;2,2;3,3;5,37,27,17,18,28,38,48,58,68,78;5,31,21,22,32,42,52;5,54,44,34,24,23,33,43;5,73,74,75,85,95,96,86,76,66,56,46,36;4,2;4,5;5,53,63,64,65,55,45;4,5;4,2;4,2;5,82,92,91,90,80,70;3,3;5,83,93,94,84;5,97,98,88',
        '6_7_14_9_6_8_5_7_6_12_6_7_8_5_6_6_5_8_6_8_14_5_8_9_1_7_11_3_13_8;4,3;2,7;4,2;4,6;2,2;4,2;1,2;2,3;1,4;4,5;4,2;2,2;1,2;3,4;4,3;4,3;2,3;3,4;4,4;3,4;4,5;3,2;4,5;1,3;3,4;1,3;4,3;2,2;1,3;1,6;2,2;1,2;3,2;1,2;1,9;2,2;2,9;1,4;2,15;1,2;2,3;4,2;4,2;4,2;4,2;2,4;1,2;3,4;2,4;1,6;1,14;4,2;4,2;3,2;4,2;1,8;4,2;3,2;2,8',
        '9_9_11_13_8_5_7_1_2_4_9_6_6_12_10_5_8_10_6_5_11_7_12_6_8_2_4_9_9_10;5,4,3,2,1,0,15,30,45;5,27,28,29,14,13,12,11,10,9,8,7,6,5,20;4,2;5,62,61,46,47,32,17;5,34,33,18,19;2,6;5,35,36,51,50,49,48;1,2;5,39,40,41,42,43,44,59,58;5,68,53,52,67,66;4,2;5,71,70,55,56,57;5,86,85,84,83,82,81,80,79,78,77,76,75,60;1,3;3,2;5,88,89,74,73;5,109,108,107,106,105,90,91,92,93,94,95,96,97,98,99,100;2,4;5,216,201,186,171,156,141,126,111,110;3,3;5,113,114,115,116,117,118,119,134,149;5,120,135,136,137,138;5,121,122,123,124,125,140,139;5,174,159,144,143,128,129;5,175,160,145,130,131,146;5,132,147,148,133;5,151,150,165,166,167,168,169,170,155,154,153,152;5,173,158,157;4,2;5,193,192,177,162;5,178,163,164;5,191,190,189,188,187,172;5,179,194,209,208,207,206,205,204,219;5,195,180,181;5,196,197,198,199,200,185,184,183,182;5,203,202,217,218;1,4;2,2;2,3;2,2'
    ]

    task = TASKS[1]

    solution = solve_thermometers( task, print_task= True, print_solution= True )
    
    print( f'task     = \'{task}\'' )
    print( f'solution = \'{solution}\'')
    