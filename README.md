# Classic 9x9 Sudoku Solver

An algorithm that solves any valid classic 9x9 sudoku board. Created with constraint programming using the [pychoco](https://pypi.org/project/pychoco/) library.

The rules of classic sudoku can be found [here](https://en.wikipedia.org/wiki/Sudoku).

## Input

```python
def solve(grid: str, placeholder: str = ".")
```

- **grid**: an 81 character string representing a 9x9 sudoku grid
- **placeholder**: unknown values within the grid, defaults to .

## Output

If the given input is valid, the solver will display the solution in a grid format.

```
SOLUTION FOUND
8 1 2 | 7 5 3 | 6 4 9 
9 4 3 | 6 8 2 | 1 7 5 
6 7 5 | 4 9 1 | 2 8 3 
---------------------
1 5 4 | 2 3 7 | 8 9 6 
3 6 9 | 8 4 5 | 7 2 1 
2 8 7 | 1 6 9 | 5 3 4 
---------------------
5 2 1 | 9 7 4 | 3 6 8 
4 3 8 | 5 2 6 | 9 1 7 
7 9 6 | 3 1 8 | 4 5 2 
```

A grid that does not follow fundamental sudoku rules will have no solution.

```
NO SOLUTION FOUND
```
 
