from pychoco import Model


def get_square(grid, n):
    sq_row = n // 3
    sq_col = n % 3
    return [grid[r+(3*sq_row)][c+(3*sq_col)] for r in range(3) for c in range(3)]


def solve(grid, placeholder="."):
    model = Model("Sudoku Solver")
    # create 9x9 grid
    model_grid = model.intvars((9, 9), 1, 9)
    count = 0
    for r in range(9):
        for c in range(9):
            # if the value for a cell is given
            if grid[count] != placeholder:
                model_grid[r][c] = model.intvar(int(grid[count]))
            count += 1
    # define row, column and square constraints
    for n in range(9):
        model.all_different(model_grid[n]).post()
        model.all_different([model_grid[r][n] for r in range(9)]).post()
        model.all_different(get_square(model_grid, n)).post()
    solution = model.get_solver().solve()
    if solution:
        print("\n\nSOLUTION FOUND!")
        # convert grid to string
        solution_grid = "".join([str(item.get_value()) for row in model_grid for item in row])
        display(solution_grid)
    else:
        print("\n\nNO SOLUTION FOUND")


def display(grid: str):
    if not grid:
        print("Invalid sudoku board")
    count = 0
    # loop through all values
    for r in range(9):
        if r != 0 and r % 3 == 0:
            print(21 * "-") # horizontal break every 3 lines
        for c in range(9):
            if c != 0 and c % 3 == 0:
                print("| ", end="") # vertical break every 3 columns
            print(grid[count] + " ", end="")
            count += 1
        print("\n", end="")


if __name__=="__main__":
    puzzle = '8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..'
    solve(puzzle)