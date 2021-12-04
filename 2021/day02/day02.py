def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_course_product():
    inp = get_input()
    fwd = 0
    depth = 0
    for _ in inp:
        cmd, num = _.split()
        num = int(num)
        if cmd[0] == 'f':
            fwd += num
        elif cmd[0] == 'd':
            depth += num
        else:
            depth -= num
            if depth < 0:
                depth = 0
    return fwd * depth


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_course_product()
    elif i == '2':
        ans = None
    print(ans)
