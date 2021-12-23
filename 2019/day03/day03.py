def get_input():
    with open('input.txt') as file:
        inp = [w.split(',') for w in file.read().splitlines()]
    return inp


def md(coord):
    return abs(coord[0]) + abs(coord[1])


def get_nearest_intersection_md():
    inp = get_input()
    wires = [set(), set()]
    for i, w in enumerate(inp):
        curr = (0, 0)
        for d in w:
            letter, num = d[0], int(d[1:])
            inc = 1
            if letter in ('L', 'D'):
                inc = -1
            if letter in ('R', 'L'):
                for _ in range(num):
                    curr = (curr[0] + inc, curr[1])
                    wires[i].add(curr)
            else:
                for _ in range(num):
                    curr = (curr[0], curr[1] + inc)
                    wires[i].add(curr)
    wires[0] = list(wires[0])
    wires[0].sort(key=md)
    for point in wires[0]:
        if point in wires[1]:
            return md(point)
    return None


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_nearest_intersection_md()
    elif ipt == '2':
        ans = None
    print(ans)
