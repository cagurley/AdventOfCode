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


def merge_ranges(ranges):
    ranges.sort()
    i = 1
    while i < len(ranges):
        if ranges[i][0] <= ranges[i-1][1]:
            ranges[i-1] = (ranges[i-1][0], max((ranges[i-1][1], ranges[i][1])))
            del ranges[i]
        else:
            i += 1
    return None


def get_total_fresh():
    ranges, ids = get_input()
    merge_ranges(ranges)
    fresh = 0
    for id in ids:
        for i, r in enumerate(ranges):
            if r[1] >= id:
                if r[0] <= id:
                    fresh += 1
                    break
    return fresh


def get_possible_fresh():
    ranges, _ = get_input()
    merge_ranges(ranges)
    fresh = 0
    for r in ranges:
        fresh += r[1] - r[0] + 1
    return fresh


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_fresh()
    elif ipt == '2':
        ans = get_possible_fresh()
    print(ans)
