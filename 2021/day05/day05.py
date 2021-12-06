import re


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def count_hv_point_overlap():
    inp = get_input()
    pts = {}
    cnt = 0
    for _ in inp:
        c = re.findall(r'\d+', _)
        c = [int(n) for n in c]
        if c[0] == c[2]:
            y = [c[1], c[3]]
            y.sort()
            y[1] += 1
            if c[0] not in pts:
                pts[c[0]] = {}
            for n in range(*y):
                if n in pts[c[0]]:
                    pts[c[0]][n] += 1
                else:
                    pts[c[0]][n] = 1
        elif c[1] == c[3]:
            x = [c[0], c[2]]
            x.sort()
            x[1] += 1
            for n in range(*x):
                if n not in pts:
                    pts[n] = {}
                if c[1] in pts[n]:
                    pts[n][c[1]] += 1
                else:
                    pts[n][c[1]] = 1
    for x in pts:
        for y in pts[x]:
            if pts[x][y] > 1:
                cnt += 1
    return cnt


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = count_hv_point_overlap()
    elif i == '2':
        ans = None
    print(ans)
