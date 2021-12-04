def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def count_increases():
    inp = get_input()
    cnt = 0
    prev = int(inp[0])
    for _ in range(1, len(inp)):
        curr = int(inp[_])
        if curr > prev:
            cnt += 1
        prev = curr
    return cnt


def count_tri_increases():
    inp = [int(_) for _ in get_input()]
    cnt = 0
    for _ in range(3, len(inp)):
        if inp[_] > inp[_-3]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = count_increases()
    elif i == '2':
        ans = count_tri_increases()
    print(ans)
