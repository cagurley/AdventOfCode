from collections import deque


def get_input():
    with open('input.txt') as file:
        inp = file.read().strip().split(',')
    return inp


def count_80():
    elapsed = 0
    fish = deque([0 for _ in range(9)])
    count = 0
    for _ in get_input():
        fish[int(_)] += 1
    while elapsed < 80:
        new = fish.popleft()
        fish[6] += new
        fish.append(new)
        elapsed += 1
    for _ in fish:
        count += _
    return count


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = count_80()
    elif i == '2':
        ans = None
    print(ans)
