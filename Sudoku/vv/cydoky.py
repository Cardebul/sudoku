
q = [[8, 1, 0, 0, 2, 0, 0, 9, 6],
    [0, 0, 7, 0, 0, 0, 2, 0, 0],
    [0, 6, 0, 0, 4, 0, 0, 5, 0],
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [0, 0, 5, 0, 6, 0, 1, 0, 0],
    [0, 0, 0, 3, 0, 5, 0, 0, 0], 
    [0, 2, 0, 0, 7, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 0, 9, 0, 0], 
    [3, 8, 0, 0, 5, 0, 0, 7, 2],]


def rounder(row, col):
    ROW = (row//3)*3+3
    COL = (col//3)*3+3
    return (row//3)*3, ROW, (col//3)*3, COL


def pos(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return False


def val(grid, r, c):
    all = set(i for i in range(1, 10))
    values = set()
    row, col = r, c
    for i in grid[row]:
        if i != 0:
            values.add(i)
    for j in range(col, col+1):
        for i in range(9):
            if grid[i][j] != 0:
                values.add(grid[i][j])
    q, w, e, r = rounder(row, col)
    for i in range(q, w):
        for j in range(e, r):
            if grid[i][j] != 0:
                values.add(grid[i][j])

    return list(all.difference(values))


def solve(grid):
    if not pos(grid):
        return grid
    I, J = pos(grid)
    values = val(grid, I, J)
    for i in values:
        grid[I][J] = i
        if not solve(grid):
            grid[I][J] = 0
            continue
        return solve(grid)
    return False
