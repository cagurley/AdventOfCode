def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_power_consumption():
    inp = get_input()
    counts = [[0, 0] for _ in range(len(inp[0]))]
    gamma = ''
    epsilon = ''
    for bstr in inp:
        for idx, _ in enumerate(bstr):
            counts[idx][int(_)] += 1
    for _ in counts:
        if _[1] > _[0]:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def get_life_support_rating():
    inp = get_input()
    inp.sort()
    nlen = len(inp[0])
    rlen = len(inp)

    a = 0
    b = rlen - 1
    for n in range(nlen):
        if a == b:
            break
        m = a + 1
        while m <= b and inp[m][n] == inp[m-1][n]:
            m += 1
        if m > b:
            pass
        elif (m - a) > (b + 1 - m):
            b = m - 1
        else:
            a = m
    oxy = int(inp[b], 2)

    a = 0
    b = rlen - 1
    for n in range(nlen):
        if a == b:
            break
        m = a + 1
        while m <= b and inp[m][n] == inp[m-1][n]:
            m += 1
        if m > b:
            pass
        elif (m - a) > (b + 1 - m):
            a = m
        else:
            b = m - 1
    co2 = int(inp[a], 2)

    return oxy * co2


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_power_consumption()
    elif i == '2':
        ans = get_life_support_rating()
    print(ans)
