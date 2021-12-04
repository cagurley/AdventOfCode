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


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_power_consumption()
    elif i == '2':
        ans = None
    print(ans)
