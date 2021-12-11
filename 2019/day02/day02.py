def get_input():
    with open('input.txt') as file:
        inp = [int(n) for n in file.read().strip().split(',')]
    return inp


def get_alarm_output(inp, noun, verb):
    inp[1] = noun
    inp[2] = verb
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


def get_sentence_by_output(output):
    inp = get_input()
    params = None
    for i in range(100):
        for j in range(100):
            if output == get_alarm_output(inp.copy(), i, j):
                params = (i, j)
            if params:
                break
        if params:
            return 100 * params[0] + params[1]


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_alarm_output(get_input(), 12, 2)
    elif ipt == '2':
        ans = get_sentence_by_output(19690720)
    print(ans)
