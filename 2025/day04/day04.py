def get_input():
    with open('input.txt') as file:
        inp = [[c for c in line] for line in file.read().splitlines()]
    return inp


def get_accessible_rolls():
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


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_accessible_rolls()
    elif ipt == '2':
        ans = None
    print(ans)
