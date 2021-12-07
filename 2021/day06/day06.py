from collections import deque


def get_input():
    with open('input.txt') as file:
        inp = file.read().strip().split(',')
    return inp


def count_fish(days=0):
    elapsed = 0
    fish = deque([0 for _ in range(9)])
    count = 0
    for _ in get_input():
        fish[int(_)] += 1
    while elapsed < days:
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
        ans = count_fish(80)
    elif i == '2':
        ans = count_fish(256)
    print(ans)
