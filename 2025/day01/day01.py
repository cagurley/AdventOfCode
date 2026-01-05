def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_stop_password():
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


def get_rotate_password():
    count = 0
    position = 50
    for line in get_input():
        clicks = int(line[1:])
        while True:
            if clicks > 99:
                count += 1
                clicks -= 100
            else:
                if line[0] == 'L':
                    clicks = -clicks
                if position == 0:
                    position += clicks
                else:
                    position += clicks
                    if not (0 < position < 100):
                        count += 1
                position %= 100
                break
    return count


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_stop_password()
    elif ipt == '2':
        ans = get_rotate_password()
    print(ans)
