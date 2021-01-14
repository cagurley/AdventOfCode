def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    for index, line in enumerate(inp):
        inp[index] = int(line)
    inp.sort()
    return inp


def find_diff_product():
    inp = get_input()
    prev = 0
    ones = 0
    threes = 0
    for num in inp:
        diff = num - prev
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        prev = num
    threes += 1
    return ones * threes


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = find_diff_product()
    elif i == '2':
        ans = None
    print(ans)
