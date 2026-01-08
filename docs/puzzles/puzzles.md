# Puzzles

Puzzles provide a fun way to get hands-on experience with CP/MIP formulations and solvers.

## Kakurasu

Play online: [https://www.puzzle-kakurasu.com/](https://www.puzzle-kakurasu.com/)

**Kakurasu.**
Given an $n\times n$ grid with target values assigned to each row and column.
The goal is to select (for example, shade) some cells so that the sum of the indices of the selected cells in every row and column matches the given target values.


```text
Instance:         Solution:      
    1 2 3 4           1 2 3 4    
  ┌─────────┐       ┌─────────┐  
1 │         │ 5   1 │ ×     × │ 5
2 │         │ 4   2 │       × │ 4
3 │         │ 2   3 │   ×     │ 2
4 │         │ 8   4 │ ×   × × │ 8
  └─────────┘       └─────────┘  
    5 3 4 7           5 3 4 7    
```

Kakurasu instances are encoded as strings that consist of the target values for columns (from left to right) and for rows (from top to bottom) separated by slashes (`'/'`).
For example, the instance shown above is encoded as:
```python
kakurasu_instance = '5/3/4/7/5/4/2/8'
```

## Skyscrapers

Play online: [https://www.puzzle-skyscrapers.com/](https://www.puzzle-skyscrapers.com/)

**Skyscrapers (Skylines, Towers).**
Given an $n\times n$ grid with clues along the edges (top, bottom, left, right) and some pre-filled cells.
The goal is to fill the remaining cells with numbers $1,\ldots,n$ – representing skyscrapers of that heights – such that:

- Each number appears exactly once in every row and every column.
- Each edge clue indicates how many skyscrapers are visible from that direction in the corresponding row or column.
Note that a taller skyscraper blocks the view of any shorter skyscraper behind it.

```text
Instance:           Solution:       
          2                   2      
  ┌───────────┐       ┌───────────┐  
4 │ · · · · · │     4 │ 2 1 3 4 5 │  
  │ · · · · · │ 4     │ 5 4 1 3 2 │ 4
  │ · · · · · │       │ 4 2 5 1 3 │  
  │ · · · · 1 │       │ 1 3 2 5 4 │  
  │ · · 2 · · │       │ 3 5 4 2 1 │  
  └───────────┘       └───────────┘  
    3     2             3     2      
```

Skyscrapers instances are encoded as strings, as follows.
The string consists of one or two parts, separated by a comma `','` in the latter case.
The first part encodes the clues for columns (top and bottom, from left to right) and for rows (left and right, from top to bottom), separated by slashes `'/'`, using `''` for missing clues.
The optional second part encodes the grid itself.
Cells are listed consecutively, row by row.
If a cell contains a number, the number is written directly; if it is empty, the number of consecutive empty cells until the next pre-given number (or until the end) is represented by a single character: `'a'` for 1 empty cell, `'b'` for 2 empty cells, `'c'` for 3 empty cells, etc.
Underscores `'_'` can optionally be used to separate adjacent numbers for readability.
For example, the instance shown above is encoded as:
```python
skyscrapers_instance = '///2//3///2//4//////4///,s1b2b'
```

## Binario

Play online: [https://www.puzzle-binairo.com/](https://www.puzzle-binairo.com/)

**Binario (Takuzu)**.
Given a $2n \times 2n$ grid, some cells may already be filled with black or white circles.
The goal is to fill the remaining cells with black and white circles so that:

- Each row and each column contains exactly $n$ black circles and $n$ white circles.
- No row or column contains three consecutive circles of the same color.
- All rows are pairwise distinct, and all columns are pairwise distinct.

```text
Instance:       Solution:
┌─────────────┐ ┌─────────────┐ 
│ 0 0 · · · · │ │ 0 0 1 0 1 1 │  0: white circle
│ · · 1 · · · │ │ 1 0 1 0 1 0 │  1: black circle
│ 1 · · · · · │ │ 1 1 0 1 0 0 │
│ · · · 1 · · │ │ 0 0 1 1 0 1 │
│ · · · · · · │ │ 1 1 0 0 1 0 │
│ · 1 · · 0 1 │ │ 0 1 0 1 0 1 │
└─────────────┘ └─────────────┘
```

Binario instances are encoded as strings, as follows.
```python
binario_instance = 'f1a1b1e1a0g1d11b'
```

## Slitherlink

Play online: [https://www.puzzle-loop.com/](https://www.puzzle-loop.com/)

**SlitherLink (Loops, Fences).**
Given an $n \times n$ grid, where some cells contain a number from 0 to 3.
The goal is to draw a single, non-crossing loop along the edges of the cells such that the number in each cell indicates how many of its sides are crossed by the loop.

```text
Instance:                 Solution:
·   ·   ·   ·   ·   ·     ·   ┌───┐   ·   ┌───┐ 
  2       1   2             2 │   │ 1   2 │   │ 
·   ·   ·   ·   ·   ·     ┌───┘   │   ┌───┘   │ 
  3   1                   │ 3   1 │   │       │ 
·   ·   ·   ·   ·   ·     └───┐   └───┘   ┌───┘ 
  3           1             3 │         1 │     
·   ·   ·   ·   ·   ·     ┌───┘   ┌───┐   └───┐ 
  2               2       │ 2     │   │     2 │ 
·   ·   ·   ·   ·   ·     │   ┌───┘   └───┐   │ 
      2   0   2           │   │ 2   0   2 │   │ 
·   ·   ·   ·   ·   ·     └───┘   ·   ·   └───┘ 
```

Slitherlink instances are encoded as strings, as follows.
Cells are listed consecutively, row by row.
If a cell contains a number, the number is written directly; if it is empty, the number of consecutive empty cells until the next number (or until the end) is represented by a single character: `'a'` for 1 empty cell, `'b'` for 2 empty cells, `'c'` for 3 empty cells, etc.
For example, the instance shown above is encoded as:
```python
slitherlink_instance = '2a12a31c3b1a2c2a202a'
```

## Hashi

Play online: [https://www.puzzle-bridges.com/](https://www.puzzle-bridges.com/)

**Hashi (Bridges).**
Given an $n\times n$ grid, where some cells contain a number between 1 and 8 representing islands.
The goal is to connect all islands into a single connected group using bridges, subject to the following rules:

- Each bridge connects exactly two islands in a straight line.
- Bridges run only horizontally or vertically.
- Bridges cannot cross other bridges or islands.
- At most two bridges can connect any pair of islands.
- The number of bridges connected to each island must equal the number written on that island.

```text
Instance:                      Solution:
·   4   ·   ·   ·   ·   3      ·   4 ═════════════════ 3
                                   ║                   │
2   ·   4   ·   ·   4   ·      2   ║   4 ═════════ 4   │
                               ║   ║   ║           ║   │
·   2   ·   ·   ·   ·   ·      ║   2   ║   ·   ·   ║   │
                               ║       ║           ║   │
·   ·   ·   ·   ·   2   ·      ║   ·   ║   ·   ·   2   │
                               ║       ║               │
3   ·   4   ·   ·   ·   4      3 ───── 4 ───────────── 4
                                                       ║
·   ·   ·   ·   ·   ·   ·      ·   ·   ·   ·   ·   ·   ║
                                                       ║
·   1   ·   2   ·   ·   3      ·   1 ───── 2 ───────── 3
```

Hashi instances are encoded as strings, as follows.
Cells are listed consecutively, row by row.
If a cell contains a number, the number is written directly; if it is empty, the number of consecutive empty cells until the next number (or until the end) is represented by a single character: `'a'` for 1 empty cell, `'b'` for 2 empty cells, `'c'` for 3 empty cells, etc.
For example, the instance shown above is encoded as:
```python
hashi_instance = 'a4d32a4b4b2j2a3a4c4h1a2b3'
```

## Masyu

Play online: [https://www.puzzle-masyu.com/](https://www.puzzle-masyu.com/)

**Masyu.**
Given an $n\times n$ grid, where some cells contain a black or a white circle.
The goal is to draw a single non-crossing loop that passes through all the circles, subject to the following rules:

- The loop moves only along the centers of cells, horizontally or vertically.
- The loop must turn on black circles, and must go straight in the cells immediately before **and** after each black circle.
- The loop must go straight through white circles, and must turn in at least one of the cells immediately before **or** after each white circle.

```text
Instance:                  Solution:            
·   ·   ·   ·   W   B      ┌───┐   ·   ┌── W ─ B      W: white circle 
                           │   │       │       │      B: black circle
W   ·   W   ·   ·   W      W   └── W ──┘   ·   W
                           │                   │
·   ·   ·   B   ·   ·      │   ┌────── B   ┌───┘
                           │   │       │   │    
·   W   ·   W   W   ·      │   W   ·   W   W   ·
                           │   │       │   │    
W   W   ·   ·   ·   ·      W   W   ·   │   └───┐
                           │   │       │       │
·   ·   ·   B   ·   ·      └───┘   ·   B ──────┘
```

Masyu instances are encoded as strings, as follows.
Cells are listed consecutively, row by row.
If a cell contains a white or a black circle, the upper case letter `'W'` or `'B'` is written, respectively; if it is empty, the number of consecutive empty cells until the next number (or until the end) is represented by a single lower case letter: `'a'` for 1 empty cell, `'b'` for 2 empty cells, `'c'` for 3 empty cells, etc.
For example, the instance shown above is encoded as:
```python
masyu_instance = 'dWBWaWbWcBcWaWWaWWgBb'
```

## Hitori

Play online: [https://www.puzzle-hitori.com/](https://www.puzzle-hitori.com/)

**Hitori.**
Given an $n\times n$ grid where each cell contains a number from $1$ to $n$.
The goal is to mark (for example, shade) some cells such that:

- In every row and column, the unmarked numbers are all distinct.
- Marked cells cannot be adjacent horizontally or vertically.
- All unmarked cells form a single connected group.

```text
Instance:     Solution:
┌───────────┐ ┌───────────┐
│ 1 5 4 4 3 │ │ 1 5 ▒ 4 ▒ │
│ 3 3 1 2 5 │ │ ▒ 3 1 2 5 │
│ 3 1 1 5 3 │ │ 3 1 ▒ 5 ▒ │
│ 1 2 4 3 1 │ │ ▒ 2 4 3 1 │
│ 2 4 5 5 3 │ │ 2 4 5 ▒ 3 │
└───────────┘ └───────────┘
```

Hitori instances are encoded as strings, where cells are listed consecutively, row by row.
For example, the instance shown above is encoded as:
```python
hitori_instance = '1544333125311531243124553'
```

## Pipes

Play online: [https://www.puzzle-pipes.com/](https://www.puzzle-pipes.com/)

**Pipes.**
Given an $n\times n$ grid where each cell contains a pipe tile.
The goal is to rotate the tiles so that they form a single connected network without cycles.

```text
Instance:    Solution:
╵╴╵┘         ╷╷╶┐ 
┬├─┴         ├┴─┤ 
╴┘┬┬         ╵┌┬┤ 
╷└╷╴         ╶┘╵╵ 
```

Pipes instances are encoded as strings, where cells (see the next table for encoding characters) are listed consecutively, row by row.

char  | tile | description    | char  | tile | description
:----:|:----:|:---------------|:-----:|:----:|:--------------
**1** | ╶    | sink     (r)   | **8** | ╷    | sink     (d)
**2** | ╵    | sink     (u)   | 9     | ┌    | curve    (rd)
3     | └    | curve    (ru)  | a     | │    | straight (ud)
**4** | ╴    | sink     (l)   | b     | ├    | branch   (rud)
5     | ─    | straight (rl)  | c     | ┐    | curve    (ld)
6     | ┘    | curve    (ul)  | d     | ┬    | branch   (rld)
7     | ┴    | branch   (rul) | e     | ┤    | branch   (uld)


For example, the instance shown above is encoded as:
```python
pipes_instance = '2426db5746dd8384'
```
