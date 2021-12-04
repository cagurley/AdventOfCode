def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def convert(string):
    row = 0
    row_part = 64
    col = 0
    col_part = 4
    for n, c in enumerate(string):
        if n < 7:
            if c == 'B':
                row += row_part
            row_part //= 2
        else:
            if c == 'R':
                col += col_part
            col_part //= 2
    return row, col


def get_id(string):
    row, col = convert(string)
    return row * 8 + col


def find_max_id():
    max_id = -1
    for string in get_input():
        sid = get_id(string)
        if sid > max_id:
            max_id = sid
    return max_id


def find_missing_id():
    ids = []
    for string in get_input():
        ids.append(get_id(string))
    ids.sort()
    lower = 1
    part = (len(ids) - 1) // 2
    while part > 0:
        if ids[lower + part] == ids[lower] + part:
            lower += part + 1
        part //= 2
    return ids[lower] + 1


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = find_max_id()
    elif i == '2':
        ans = find_missing_id()
    print(ans)
