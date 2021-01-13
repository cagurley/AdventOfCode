def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def run_until_repeat():
    inp = get_input()
    acc = 0
    line = 0
    executed = set()
    while True:
        executed.add(line)
        ins, val = inp[line].split()
        val = int(val)
        if ins == 'jmp':
            if val < 0 and (line + val) in executed:
                return acc
            line += val
        else:
            if ins == 'acc':
                acc += val
            line += 1


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = run_until_repeat()
    elif i == '2':
        ans = None
    print(ans)
