def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def count_increases():
    inp = get_input()
    count = 0
    prev = int(inp[0])
    for _ in range(1, len(inp)):
        curr = int(inp[_])
        if curr > prev:
            count += 1
        prev = curr
    return count


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = count_increases()
    elif i == '2':
        ans = None
    print(ans)
