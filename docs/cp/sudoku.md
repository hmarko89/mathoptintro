---
tags:
  - cp
  - puzzle
---

# Sudoku

Play online: [www.puzzle-sudoku.com](https://www.puzzle-sudoku.com/)

## Rules

There is a *grid* of size $9\times 9$.
The goal is to write a number from $1,\ldots,9$ in each cell, such that each column, each row, and each of the nine $3\times 3$ subgrids that compose the grid contains all numbers exactly once.
Some numbers are pre-given.

For example:
```text
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
If cell $(i,j)$ is empty, the corresponding domain is $\{1,\ldots,9\}$, otherwise the variable is fixed to he given value.

$$
D_{ij} = 
\begin{cases}
\{G_{ij}\}     & \text{if }G_{ij} \neq \emptyset\\
\{1,\ldots,9\} & \text{otherwise}
\end{cases}
$$

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
\operatorname{alldifferent}( \mathbf{x}_{i + i',j+j'} : i' = 0,1,2,\ j' = 0,1,2 )\quad \text{for all}\ i = 1,4,9,\ j = 1,4,9
$$

### Objective

There is no objective, since it is a feasibility problem.

## Implementation

For the full code, see file `src/cp/sudoku.py`.

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
def _decode_sudoku_string( task:str ) -> list[list[int]]:
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
        Filled cells are integers, empty cells are None.
    """
    cells = []

    for char in task:
        if char.isnumeric():
            cells.append( int(char) )
        elif char.isalpha():
            cells.extend( None for _ in range(96,ord(char)) )
        elif char == '_':
            continue
        else:
            raise ValueError( f'could not decode task "{task}" due to unexpected character: "{char}"' )

    assert len(cells) == 81, f'could not decode task "{task}" succesfully'

    return [ cells[9*i:9*(i+1)] for i in range(9) ]
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

### Drawing the puzzle

The following function prints a task/solution in a more-or-less fancy way:

```python
def _print_sudoku( grid:list[list[int]] ) -> None:
    """
    Prints the given instance/solution for Sudoku.
    
    Args
    ----
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Filled cells are integers, empty cells are None.
    """
    CHARS = '·' # empty 

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

            print( f' {grid[i][j] if grid[i][j] != None else CHARS[0]}', end= '' )
```

### Solver

We use the package ```ortools.sat.python.cp_model``` for the implementation.

```python
import itertools as it

def _solve_sudoku( grid:list[list[int]] ) -> list[list[int]]:
    """
    Solves Sudoku as CP with OR-Tools CP-SAT Solver.
    
    Args
    ----
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
        Filled cells are integers, empty cells are None.

    Returns
    -------
    grid : list[list[int]]
        A 9x9 Sudoku grid as a list of row-lists.
    """
    from ortools.sat.python import cp_model

    n = 3 
    N = range(n*n)

    assert len(grid) == n*n, 'invalid matrix size!'

    # BUILD MODEL
    model = cp_model.CpModel()

    # variables: x[i][j] = the number written into cell (i,j)
    x = [ [ model.new_int_var( 1, n*n, f'x_{i}_{j}' ) for j in N ] for i in N ]

    # constraints: pre-given numbers
    for (i,j) in it.product(N,N):
        if grid[i][j] != None:
            model.add( x[i][j] == grid[i][j] )
    
    # constraints: each number occurs exactly once in a row
    for i in N:
        model.add_all_different( x[i][j] for j in N )

    # constraints: each number occurs exactly once in a column
    for j in N:
        model.add_all_different( x[i][j] for i in N )

    # constraints: each number occurs exactly once in a 3x3 subgrid
    for (p,q) in it.product(range(n),range(n)):
       model.add_all_different( x[i+n*p][j+n*q] for (i,j) in it.product(range(n),range(n)) )

    # SOLVE PROBLEM
    solver = cp_model.CpSolver()
    status = solver.solve( model )
    assert status == cp_model.OPTIMAL, f'status: {solver.status_name(status)}'

    # return solution
    return [ [ solver.value(x[i][j]) for j in N ] for i in N ]
```

The wrapper function (from string to string):

```python
def solve_sudoku( task:str, print_task:bool= False, print_solution:bool= False ) -> str:
    """
    Solves Sudoku as CP with OR-Tools CP-SAT Solver.
    
    Args
    ----
    task : str
        An instance for Sudoku encoded as a string, where:
        - digits '1'-'9' represent filled cells
        - letters 'a'-'z' represent consecutive empty cells
        - optional underscores '_' may be used to separate digits
    
    print_task : bool
        Should we print task?
    
    print_solution : bool
        Should we print solution?

    Returns
    -------
    solution : str
        The string that encodes the solution, where:
        - digits '1'-'9' represent filled cells
        - letters 'a'-'z' represent consecutive empty cells
        - optional underscores '_' may be used to separate digits
    """
    # process (and print) task
    grid = _decode_sudoku_string( task )
    if print_task:
        _print_sudoku( grid )

    # solve problem (and print solution)
    solution = _solve_sudoku( grid )
    if print_solution:
        _print_sudoku( solution )

    return _encode_sudoku_grid( solution )
```

An example:

```python
if __name__ == '__main__':
    task = 'b4_6b3_5f4b7_8b5d2_1a5_3c6k3c1_2a4_7d3b1_3b9f2_1b5_8b'

    solution = solve_sudoku( task, print_task= True, print_solution= True )
    
    print( f'task     = \'{task}\'')
    print( f'solution = \'{solution}\'' )
```
