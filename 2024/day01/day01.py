def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_total_distance():
    left, right = [], []
    total = 0
    for line in get_input():
        first, second = line.split()
        left.append(int(first))
        right.append(int(second))
    left.sort()
    right.sort()
    for i, x in enumerate(left):
        total += abs(x - right[i])
    return total


def get_similarity_score():
    left, right = [], {}
    total = 0
    for line in get_input():
        first, second = [int(v) for v in line.split()]
        left.append(first)
        if second in right.keys():
            right[second] += 1
        else:
            right[second] = 1
    for v in left:
        if v in right:
            total += v * right[v]
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_distance()
    elif ipt == '2':
        ans = get_similarity_score()
    print(ans)
