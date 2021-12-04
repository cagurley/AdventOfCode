def get_input():
    inp = []
    with open('input.txt') as file:
        for num in file.read().split():
            inp.append(int(num))
    inp.sort()
    return inp


def find_bi_prod():
    inp = get_input()
    left = 0
    right = len(inp) - 1
    while left < right:
        s = inp[left] + inp[right]
        if s > 2020:
            right -= 1
        elif s < 2020:
            left += 1
        else:
            return (inp[left] * inp[right]), [inp[left], inp[right]]
    return -1, (-1, -1)


def find_tri_prod():
    inp = get_input()
    left = 0
    left_max = len(inp) - 2
    right_max = left_max + 1
    while left < left_max:
        center = left + 1
        right = right_max
        while center < right:
            s = inp[left] + inp[center] + inp[right]
            if s > 2020:
                right -= 1
            elif s < 2020:
                center += 1
            else:
                return (inp[left] * inp[center] * inp[right]), [inp[left], inp[center], inp[right]]
        left += 1
    return -1, (-1, -1, -1)


if __name__ == '__main__':
    while True:
        i = input('Answer part 1 or 2?  ')
        ans = None
        if i == '1':
            ans = find_bi_prod()
            print('{}\n({}, {})'.format(ans[0], *ans[1]))
            break
        elif i == '2':
            ans = find_tri_prod()
            print('{}\n({}, {}, {})'.format(ans[0], *ans[1]))
            break
