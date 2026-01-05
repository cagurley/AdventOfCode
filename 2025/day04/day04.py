def get_input():
    with open('input.txt') as file:
        inp = [[c for c in line] for line in file.read().splitlines()]
    return inp


def get_accessible_initial():
    grid = get_input()
    accessible = 0
    row_num = len(grid)
    col_num = len(grid[0])
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                blockers = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x == i and y == j:
                            continue
                        if x > -1 < y and x < row_num and y < col_num and grid[x][y] == '@':
                            blockers += 1
                if blockers < 4:
                    accessible += 1
    return accessible


def get_accessible_iterative():
    grid = get_input()
    removable = 0
    row_num = len(grid)
    col_num = len(grid[0])
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                blockers = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x == i and y == j:
                            continue
                        if x > -1 < y and x < row_num and y < col_num and (
                            grid[x][y] == '@' or isinstance(grid[x][y], int)
                        ):
                            blockers += 1
                grid[i][j] = blockers
    loop = True
    while loop:
        loop = False
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if isinstance(c, int) and c < 4:
                    loop = True
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            if x == i and y == j:
                                continue
                            if x > -1 < y and x < row_num and y < col_num and isinstance(grid[x][y], int):
                                grid[x][y] -= 1
                    grid[i][j] = 'x'
                    removable += 1
    return removable


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_accessible_initial()
    elif ipt == '2':
        ans = get_accessible_iterative()
    print(ans)
