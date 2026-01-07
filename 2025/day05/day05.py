def get_input():
    with open('input.txt') as file:
        ranges = []
        ids = []
        mode = True
        for line in file:
            line = line.strip()
            if not line:
                mode = False
                continue
            if mode:
                line = tuple(int(v) for v in line.split("-"))
                ranges.append(line)
            else:
                ids.append(int(line))
    return ranges, ids


def get_total_fresh():
    ranges, ids = get_input()
    ranges.sort()
    fresh = 0
    i = 1
    added = []
    while i < len(ranges):
        if ranges[i][0] <= ranges[i-1][1]:
            ranges[i-1] = (ranges[i-1][0], max((ranges[i-1][1], ranges[i][1])))
            del ranges[i]
        else:
            i += 1
    for id in ids:
        for i, r in enumerate(ranges):
            if r[1] >= id:
                if r[0] <= id:
                    fresh += 1
                    added.append(id)
                    break
    return fresh


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_fresh()
    elif ipt == '2':
        ans = None
    print(ans)
