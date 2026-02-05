import itertools as it

def _decode_skyscrapers_string( task:str ) -> tuple[int,list[int],list[int],list[int],list[int],list[list[int]]]:
    """
    Decodes the given Skyscrapers instance.

    Args
    ----
    task : str
        A Skyscrapers instance encoded as a string.

    Returns
    -------
    n : int
        The size of the grid (number of rows and columns).
    top : list[int | None]
        List of visibility clues on the top side of the grid (left to right).
    bottom : list[int | None]
        List of visibility clues on the bottom side of the grid (left to right).
    left : list[int | None]
        List of visibility clues on the left side of the grid (top to bottom).
    right : list[int | None]
        List of visibility clues on the right side of the grid (top to bottom).
    grid : list[list[int | None]]
        The grid with pre-given numbers, where missing values are represented by None.
    """
    split = task.split(',')

    around = list( map( lambda x : int(x) if x != '' else None, split[0].split('/') ) )
    n = len( around ) // 4
    top , bottom, left, right = around[0:n], around[n:2*n], around[2*n:3*n], around[3*n:4*n]

    grid = None

    if 1 < len(split): # grid may be not given
        cells = []

        for char in split[1]:
            if char.isnumeric():
                cells.append( int(char) )
            elif char.isalpha():
                cells.extend( None for _ in range( 96, ord(char) ) )
            elif char == '_':
                continue
            else:
                raise ValueError( f'could not decode task "{task}" due to unexpected character: "{char}"' )

        assert len(cells) == n*n, f'could not parse task "{task}" successfully'

        grid = []
        for i in range(n):
            grid.append( cells[n*i:n*(i+1)] )

    else:
        grid = [ [ None ] * n for _ in range(n) ]

    return n, top, bottom, left, right, grid


def _encode_skyscrapers_grid( grid:list[list[int]] ) -> str:
    """
    Encodes the given Skyscrapers solution as a string.

    Args
    ----
    grid : list[list[int | None]]
        The solution grid as a list of row-lists.

    Returns
    -------
    : str
        The solution encoded as a string.
    """
    N = range(len(grid))

    string = ''

    nonempties = 0
    for (i,j) in it.product(N,N):
        if grid[i][j] != None:
            if 0 < nonempties:
                string += chr(96+nonempties)
                nonempties = 0

            string += f'{grid[i][j]}'
        else:
            nonempties += 1
    
    if 0 < nonempties:
        string += chr(96+nonempties)

    return string

def _print_skyscrapers( n:int, top:list[int], bottom:list[int], left:list[int], right:list[int], grid:list[list[int]] ) -> None:
    """
    Prints the given instance (and solution) of Skyscrapers.

    Args
    ----
    n : int
        The size of the grid (number of rows and columns).
    top : list[int | None]
        List of visibility clues on the top side of the grid (left to right).
    bottom : list[int | None]
        List of visibility clues on the bottom side of the grid (left to right).
    left : list[int | None]
        List of visibility clues on the left side of the grid (top to bottom).
    right : list[int | None]
        List of visibility clues on the right side of the grid (top to bottom).
    grid : list[list[int | None]]
        The grid as a list of row-lists.
    """    
    CHARS = '·' # empty

    print( f'    {" ".join( map( lambda num : str(num) if num != None else " ", top ) )}     ' )
    print( f'  ┌{"─"*(2*n+1)}┐  ' )

    for i in range(n):
        print( f'{left[i] if left[i] != None else " "} │ {" ".join( map( lambda num : str(num) if num != None else CHARS[0], grid[i] ) )} │ {right[i] if right[i] != None else " "}' )

    print( f'  └{"─"*(2*n+1)}┘  ' )
    print( f'    {" ".join( map( lambda num : str(num) if num != None else " ", bottom ) )}     ' )

def _solve_skyscrapers( n:int, top:list[int], bottom:list[int], left:list[int], right:list[int], grid:list[list[int]] ) -> list[list[int]]:
    """
    Solves the given Skyscrapers instance.

    Args
    ----
    n : int
        The size of the grid (number of rows and columns).
    top : list[int | None]
        List of visibility clues on the top side of the grid (left to right).
    bottom : list[int | None]
        List of visibility clues on the bottom side of the grid (left to right).
    left : list[int | None]
        List of visibility clues on the left side of the grid (top to bottom).
    right : list[int | None]
        List of visibility clues on the right side of the grid (top to bottom).
    grid : list[list[int | None]]
        The grid with pre-given numbers.

    Returns
    -------
    grid : list[list[int]]
        The filled solution grid.
    """
    print('!!! TODO: implement Skyscrapers solver !!!')

    return grid

def solve_skyscrapers( task:str, print_task:bool= False, print_solution:bool= False ) -> str:
    """
    Solves the given Skyscrapers instance.

    Args
    ----
    task : str
        A Skyscrapers instance encoded as a string.
    print_task : bool
        Should we print the task?
    print_solution : bool
        Should we print the solution?

    Returns
    -------
    : str
        The solution encoded as a string.
    """
    # decode (and print) task
    n, top, bottom, left, right, grid = _decode_skyscrapers_string( task )
    if print_task:
        _print_skyscrapers( n, top, bottom, left, right, grid )

    # solve (and print) task
    solution = _solve_skyscrapers( n, top, bottom, left, right, grid )
    if print_solution:
        _print_skyscrapers( n, top, bottom, left, right, solution )

    return _encode_skyscrapers_grid( solution )

if __name__ == '__main__':
    TASKS = [
        '///2//3///2//4//////4///,s1b2b',
        '1/2/2/3/2/2/3/1/1/2/2/2/4/2/3/1',
        '/3//1/////3/1//////3',
        '////3/2///////4///,e4j',
        '3/5/2/1/2/2/1/2/3/2/3/2/1/3/2/2/1/3/2/2',
        '3//1//3///3//////2/4////4/',
        '4//3///////4//3//3/////2/4',
        '4/3/2/3/2/1/1/2/3/2/3/2/4/2/3/2/4/1/1/4/2/2/3/2,b1i2i1b2j',
        '4/3////3///4//4////2//3/2///3///2,a3ze3b',
        '/3/4/3//3//////2///4///2//4//2/4/,v1f1c2b',
    ]
    
    task = TASKS[0]
    
    solution = solve_skyscrapers( task, print_task= True, print_solution= True )
    
    print( f'task     = \'{task}\'')
    print( f'solution = \'{solution}\'' )
    