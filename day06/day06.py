def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    inp.append('')
    return inp


def get_any_total():
    inp = get_input()
    total = 0
    record = ''
    for line in inp:
        if line:
            record += line
        else:
            resp = set(record)
            total += len(resp)
            record = ''
    return total


def get_all_total():
    inp = get_input()
    total = 0
    group = []
    for line in inp:
        if line:
            group.append(set(line))
        else:
            resp = set.intersection(*group)
            total += len(resp)
            group.clear()
    return total


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_any_total()
    elif i == '2':
        ans = get_all_total()
    print(ans)
