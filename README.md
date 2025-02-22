# Classic 9x9 Sudoku Solver

An algorithm that solves any valid classic 9x9 sudoku board. Created with constraint programming using the [pychoco](https://pypi.org/project/pychoco/) library.

The rules of classic sudoku can be found [here](https://en.wikipedia.org/wiki/Sudoku).

## Input

```python
def solve(grid: list[int])
```

- **grid**: a 9x9 sudoku grid represented as a 2d list (unknown values should be set to 0)

## Output

If the given input is valid, the solver will display the solution in a grid format.

```
Solution Found.
[8, 6, 2, 4, 1, 3, 5, 9, 7]
[5, 9, 3, 6, 7, 8, 2, 1, 4]
[1, 7, 4, 5, 9, 2, 8, 6, 3]
[2, 5, 9, 3, 8, 7, 1, 4, 6]
[3, 1, 6, 9, 4, 5, 7, 2, 8]
[7, 4, 8, 1, 2, 6, 9, 3, 5]
[4, 3, 1, 7, 5, 9, 6, 8, 2]
[6, 8, 5, 2, 3, 1, 4, 7, 9]
[9, 2, 7, 8, 6, 4, 3, 5, 1]
```

A grid that does not follow fundamental sudoku rules will have no solution.

```
No Solution Found.
```
 
