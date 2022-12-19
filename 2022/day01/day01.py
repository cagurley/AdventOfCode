def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
        inp.append('')
    return inp


def get_max_total():
    inp = get_input()
    max_total = 0
    i = 0
    while i < len(inp):
        total = 0
        while inp[i]:
            total += int(inp[i])
            i += 1
        if max_total < total:
            max_total = total
        i += 1
    return max_total


def get_top3_total():
    inp = get_input()
    totals = []
    i = 0
    while i < len(inp):
        total = 0
        while inp[i]:
            total += int(inp[i])
            i += 1
        totals.append(total)
        i += 1
    totals.sort()
    return sum(totals[-3:])


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_max_total()
    elif ipt == '2':
        ans = get_top3_total()
    print(ans)
