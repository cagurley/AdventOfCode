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


def get_largest_basin_product():
    inp = get_input()
    h = len(inp)
    w = len(inp[0])
    basins = []
    for y in range(h):
        row = []
        basin = {y: set()}
        for x in range(w):
            if inp[y][x] < 9:
                basin[y].add(x)
            else:
                if basin[y]:
                    row.append(basin.copy())
                basin = {y: set()}
        for r in row:
            joins = []
            for n, b in enumerate(basins):
                if y-1 in b:
                    if b[y-1] & r[y]:
                        joins.append(n)
            if joins:
                existing = [basins[_] for _ in joins]
                joins.reverse()
                for _ in joins:
                    basins.pop(_)
                for _ in existing:
                    for k, v in _.items():
                        if k in r:
                            r[k] |= v
                        else:
                            r[k] = v
            basins.append(r)
    sizes = []
    for basin in basins:
        size = 0
        for v in basin.values():
            size += len(v)
        sizes.append(size)
    sizes.sort()
    return sizes[-3] * sizes[-2] * sizes[-1]



if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_low_point_risk_sum()
    elif ipt == '2':
        ans = get_largest_basin_product()
    print(ans)
