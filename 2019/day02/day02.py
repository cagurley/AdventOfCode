def get_input():
    with open('input.txt') as file:
        inp = [int(n) for n in file.read().strip().split(',')]
    return inp


def get_alarm_0():
    inp = get_input()
    inp[1] = 12
    inp[2] = 2
    i = 0
    while inp[i] != 99:
        if inp[i] not in (1, 2):
            raise ValueError('Unknown opcode')
        if inp[i] == 1:
            inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
        else:
            inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
        i += 4
    return inp[0]


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_alarm_0()
    elif ipt == '2':
        ans = None
    print(ans)
