def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_password():
    count = 0
    position = 50
    for line in get_input():
        clicks = int(line[1:])
        if line[0] == 'L':
            clicks = -clicks
        position = (position+clicks) % 100
        if position == 0:
            count += 1
    return count


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_password()
    elif ipt == '2':
        ans = None
    print(ans)
