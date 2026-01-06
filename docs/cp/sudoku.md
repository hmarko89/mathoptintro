---
tags:
  - cp
  - puzzle
---

# Sudoku

Play online: [www.puzzle-sudoku.com](https://www.puzzle-sudoku.com/)

## Rules

There is a *grid* of size $9\times 9$.
The goal is to write a number from $1,\ldots,9$ in each cell, such that each column, each row, and each of the nine $3\times 3$ subgrids that compose the grid contains all numbers.
Some numbers are pre-given.

!!! example "Example"
    ```
    Task:                         Solution:
    ┌───────┬───────┬───────┐     ┌───────┬───────┬───────┐
    │ · · 4 │ 6 · · │ 3 5 · │     │ 2 1 4 │ 6 8 7 │ 3 5 9 │
    │ · · · │ · · 4 │ · · 7 │     │ 5 9 3 │ 1 2 4 │ 6 8 7 │
    │ 8 · · │ 5 · · │ · · 2 │     │ 8 6 7 │ 5 3 9 │ 1 4 2 │
    ├───────┼───────┼───────┤     ├───────┼───────┼───────┤
    │ 1 · 5 │ 3 · · │ · 6 · │     │ 1 7 5 │ 3 4 2 │ 9 6 8 │
    │ · · · │ · · · │ · · · │     │ 4 8 2 │ 7 9 6 │ 5 1 3 │
    │ · 3 · │ · · 1 │ 2 · 4 │     │ 6 3 9 │ 8 5 1 │ 2 7 4 │
    ├───────┼───────┼───────┤     ├───────┼───────┼───────┤
    │ 7 · · │ · · 3 │ · · 1 │     │ 7 5 8 │ 2 6 3 │ 4 9 1 │
    │ 3 · · │ 9 · · │ · · · │     │ 3 4 6 │ 9 1 8 │ 7 2 5 │
    │ · 2 1 │ · · 5 │ 8 · · │     │ 9 2 1 │ 4 7 5 │ 8 3 6 │
    └───────┴───────┴───────┘     └───────┴───────┴───────┘
    ```

## CP formulation

Rows and columns are indexed from 1 to 9 (left to right, and top to bottom, respectively).
Let $G_{ij}$ denote the pre-given number for cell $(i,j)$, if any, otherwise $G_{ij} = \emptyset$.

### Variables

Let variable $\mathbf{x}_{ij}$ indicate the number written into cell $(i,j)$.
If cell $(i,j)$ is empty, the corresponding domain is $D_{i,j} = \{1,\ldots,9\}$, otherwise the variable is fixed to he given value, that is, $D_{i,j} = \{ G_{ij} \}$.

### Constraints

Each number occurs exactly once in a row:

$$
\operatorname{alldifferent}( \mathbf{x}_{i,j} : j = 1,\ldots,9 )\quad \text{for all}\ i=1,\ldots,9
$$

Each number occurs exactly once in a column:

$$
\operatorname{alldifferent}( \mathbf{x}_{i,j} : i = 1,\ldots,9 )\quad \text{for all}\ j=1,\ldots,9
$$

Each number occurs exactly once in a subgrid:

$$
\operatorname{alldifferent}( \mathbf{x}_{i + i',j+j'} : i' = 0,\ldots,2,\ j' = 0,\ldots,2 )\quad \text{for all}\ i = 1,\ldots,3,\ j = 1,\ldots,3
$$

### Objective

There is no objective, since it is a feasibility problem.

## Implementation

### Input format

Instances are encoded as strings.
For example, the instance shown above is given as:
```python
task = 'b4_6b3_5f4b7_8b5d2_1a5_3c6k3c1_2a4_7d3b1_3b9f2_1b5_8b'
```

The cells of the grid are stored consecutively (rows by rows) in this string.
If a cell contains a number, then this number is written, otherwise, the number of empty cells until the next pre-given number (or until the end) is indicated with a single character (```'a'```: 1 empty cell,  ```'b'```: 2 empty cells,  ```'c'```: 3 empty cells, etc.).
Note that this substring may contain underscores to separate adjacent numbers.
For example, ```'b4_6b'```.

The following function decodes such a string:
```python
def __decode_sudoku_string( task:str ) -> list[list[int]]:
    """
    Decodes the given instance for Sudoku.
    
    Args
    ----
    task : str
        An instance for Sudoku encoded as a string, where:
        - digits '1'-'9' represent filled cells
        - letters 'a'-'z' represent consecutive empty cells
        - optional underscores '_' may be used to separate digits

    Returns
    -------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Pre-given cells are integers, empty cells are None.
    """
    cells = []

    for char in task:
        if char.isnumeric():
            cells.append( int(char) )
        elif char.isalpha():
            cells.extend( [None] * (ord(char) - 96 ) )
        elif char == '_':
            continue
        else:
            raise ValueError( f'could not decode task "{task}" due to unexpected character: "{char}"' )

    if len(cells) != 81:
        raise ValueError( f'could not decode task "{task}" successfully' )

    return [ cells[9*i:9*(i+1)] for i in range(9) ]
```

The following function prints a task (or a solution) in a more-or-less fancy way:

```python
def __print_sudoku( grid:list[list[int]] ) -> None:
    """
    Prints the given instance/solution for Sudoku.
    
    Parameters
    ----------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Pre-given cells are integers, empty cells are None.
    """
    EMPTY_CHAR = '·' 

    for i in range(10):
        if i == 0:
            print( '┌───────┬───────┬───────┐' )

        elif i in [3,6]:
            print( '├───────┼───────┼───────┤' )

        elif i == 9:
            print( '└───────┴───────┴───────┘' )
            break

        for j in range(10):
            if j == 0:
                print( '│', end= '' )

            elif j in [3,6]:
                print( ' │', end= '' )

            elif j == 9:
                print( ' │' )
                break

            print( f' {grid[i][j] if grid[i][j] is not None else EMPTY_CHAR}', end= '' )
```

### Output format

The filled grid is encoded as a string, where the rows are stored consecutively.
For example, the solution for the above instances is:
```python
solution = '214687359593124687867539142175342968482796513639851274758263491346918725921475836'
```

The following code encodes a task or solution:
```python
import itertools as it

def __encode_sudoku_grid( grid:list[list]) -> str:
    """
    Encodes the given instance/solution for Sudoku as a string.

    Parameters
    ----------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Pre-given cells are integers, empty cells are None.

    Returns
    -------
    task : str
        An instance/solution for Sudoku encoded as a string, where:
        - digits '1'-'9' represent filled cells
        - letters 'a'-'z' represent consecutive empty cells
    """
    task = ''

    nonempties = 0
    for (i,j) in it.product(range(9),range(9)):
        if grid[i][j] is None:
            nonempties += 1
            continue
            
        if 0 < nonempties:
            task += chr(96+nonempties)
            nonempties = 0

        task += f'{grid[i][j]}'
    
    if 0 < nonempties:
        task += chr(96+nonempties)

    return task
```

### Solver

We use ```Python-MIP``` for the implementation.

```python
import mip
import itertools as it

def __solve_sudoku( grid:list[list[int]] ) -> list[list[int]]:
    """
    Solves Sudoku.
    
    Parameters
    ----------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Filled cells are integers, empty cells are None.

    Returns
    -------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
    """
    n = 3 
    N = range(0,n*n)

    assert len(grid) == n*n, 'invalid matrix size!'

    # BUILD MODEL
    model = mip.Model( 'sudoku' )

    # variables - indicating if number k is written into cell (i,j)
    x = [ [ [ model.add_var( name= f'x_{i}_{j}_{k}', var_type= mip.BINARY ) for k in N ] for j in N ] for i in N ]

    # constraints - exactly one number in a cell
    for (i,j) in it.product(N,N):
        model += mip.xsum( x[i][j][k] for k in N ) == 1
    
    # constraints - each number occurs exactly once in a row
    for (i,k) in it.product(N,N):
        model += mip.xsum( x[i][j][k] for j in N ) == 1

    # constraints - each number occurs exactly once in a column
    for (j,k) in it.product(N,N):
        model += mip.xsum( x[i][j][k] for i in N ) == 1

    # constraints - each number occurs exactly once in a 3x3 subgrid
    for (gi,gj,k) in it.product( range(n), range(n), N ):
        model += mip.xsum( x[i][j][k] for (i,j) in it.product( range(n*gi,n*(gi+1)), range(n*gj,n*(gj+1)) ) ) == 1

    # constraints (lower bounds) - pre-given numbers
    for (i,j) in it.product(N,N):
        if grid[i][j] != None:
            x[i][j][grid[i][j]-1].lb = 1

    # SOLVE PROBLEM
    model.verbose = 0   # turn off log
    model.objective = 0 # no objective
    model.optimize()

    # return solution
    assert model.status == mip.OptimizationStatus.OPTIMAL, f'optimization status: {model.status.name}'

    return [ [ int(sum( round(x[i][j][k].x)*(k+1) for k in N )) for j in N ] for i in N ]
```

The wrapper function (from string to string):

```python
def solve_sudoku( task:str, print_task:bool= False, print_solution:bool= False ) -> str:
    """
    Solves Sudoku.
    
    Parameters
    ----------
    task: str
        An instance for Sudoku encoded as a string
    
    print_task: bool
        Should we print task?
    
    print_solution: bool
        Should we print solution?

    Returns
    -------
    solution: str
        The solution encoded as a string
    """
    # process (and print) task
    grid = __decode_sudoku_string( task )
    if print_task:
        __print_sudoku( grid )

    # solve (and print) task
    solution = __solve_sudoku( grid )
    if print_solution:
        __print_sudoku( solution )

    return __encode_sudoku_grid( solution )
```

An example:

```python
if __name__ == '__main__':
    task = 'b4_6b3_5f4b7_8b5d2_1a5_3c6k3c1_2a4_7d3b1_3b9f2_1b5_8b'

    solution = solve_sudoku( task, print_task= True, print_solution= True )
    
    print( f'task     = \'{task}\'')
    print( f'solution = \'{solution}\'' )
```
