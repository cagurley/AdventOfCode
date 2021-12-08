def get_input():
    with open('input.txt') as file:
        inp = file.read().strip().split(',')
    return inp


def get_min_align_cost():
    inp = get_input()
    inp = [int(_) for _ in inp]
    inp.sort()
    crabs = len(inp)
    mid = crabs//2
    pos = inp[mid]
    if crabs % 2 == 0:
        pos = (inp[mid-1] + pos) // 2
    fuel = 0
    for _ in inp:
        fuel += abs(_ - pos)
    return fuel



if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_min_align_cost()
    elif i == '2':
        ans = None
    print(ans)
