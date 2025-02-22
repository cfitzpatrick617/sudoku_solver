from pychoco import Model


def get_square(grid, n):
    sq_row = n // 3
    sq_col = n % 3
    return [grid[r+(3*sq_row)][c+(3*sq_col)] for r in range(3) for c in range(3)]


def solve(grid: list[str]):
    model = Model("Sudoku Solver")
    # create 9x9 grid
    model_grid = model.intvars((9, 9), 1, 9)
    for r in range(9):
        for c in range(9):
            # if the value for a cell is given
            if grid[r][c] != 0:
                model_grid[r][c] = model.intvar(grid[r][c])
    # row, column and square constraints
    for n in range(9):
        model.all_different(model_grid[n]).post()
        model.all_different([model_grid[r][n] for r in range(9)]).post()
        model.all_different(get_square(model_grid, n)).post()
    solution = model.get_solver().solve()
    if solution:
        return [[item.get_value() for item in row] for row in model_grid]
    return None


if __name__=="__main__":
    puzzle = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 2, 0, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 6, 8, 0],
        [0, 8, 5, 0, 0, 1, 0, 0, 9],
        [0, 0, 0, 0, 0, 4, 0, 0, 0]
    ]
    solution = solve(puzzle)
    if not solution:
        print("No Solution Found.")
    else:
        print("Solution Found.")
        for row in solution:
            print(row)
