def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_col_all_rows(inc):
    inp = get_input()
    collisions = 0
    pos = 0
    for row in inp:
        pos %= len(row)
        if row[pos] == '#':
            collisions += 1
        pos += inc
    return collisions


def get_col_1_2():
    inp = get_input()
    collisions = 0
    pos = 0
    check = True
    for row in inp:
        if check:
            pos %= len(row)
            if row[pos] == '#':
                collisions += 1
            pos += 1
        check = not check
    return collisions


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = -1
    if i == '1':
        ans = get_col_all_rows(3)
    elif i == '2':
        ans = get_col_all_rows(1)
        ans *= get_col_all_rows(3)
        ans *= get_col_all_rows(5)
        ans *= get_col_all_rows(7)
        ans *= get_col_1_2()
    print(ans)
