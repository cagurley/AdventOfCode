def get_yes_total():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    inp.append('')
    total = 0
    record = ''
    for line in inp:
        if line:
            record += line
        else:
            resp = set()
            resp.update(record)
            total += len(resp)
            record = ''
    return total


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_yes_total()
    elif i == '2':
        ans = None
    print(ans)
