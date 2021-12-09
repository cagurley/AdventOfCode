DIGITS = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}


def get_input():
    inp = []
    with open('input.txt') as file:
        for line in file.read().splitlines():
            line = line.split(' | ')
            for i, p in enumerate(line):
                line[i] = p.split()
            inp.append(line)
    return inp


def count_1478():
    inp = get_input()
    cnt = 0
    for disp in inp:
        for _ in disp[1]:
            if len(_) in (2, 3, 4, 7):
                cnt += 1
    return cnt


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = count_1478()
    elif ipt == '2':
        ans = None
    print(ans)
