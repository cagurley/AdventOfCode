def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    inp = [[int(_) for _ in line] for line in inp]
    return inp


def get_low_point_risk_sum():
    inp = get_input()
    h = len(inp)
    w = len(inp[0])
    risks = []
    sum = 0
    for y in range(h):
        for x in range(w):
            comps = [(x+i, y+j) for (i, j) in [(0, -1), (-1, 0), (1, 0), (0, 1)] if (-1 < x+i < w) and -1 < y+j < h]
            curr = inp[y][x]
            low = True
            for point in comps:
                if curr < inp[point[1]][point[0]]:
                    continue
                low = False
                break
            if low:
                risks.append(curr + 1)
    for _ in risks:
        sum += _
    return sum


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_low_point_risk_sum()
    elif ipt == '2':
        ans = None
    print(ans)
