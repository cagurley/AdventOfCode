def find_prod():
    inp = []
    with open('input.txt') as file:
        for num in file.read().split():
            inp.append(int(num))
    inp.sort()
    left = 0
    right = len(inp) - 1
    while left < right:
        sum = inp[left] + inp[right]
        if sum > 2020:
            right -= 1
        elif sum < 2020:
            left += 1
        else:
            return (inp[left] * inp[right]), inp[left], inp[right]
    return -1, -1, -1


if __name__ == '__main__':
    print('{}\n({}, {})'.format(*find_prod()))
