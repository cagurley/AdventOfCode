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


def fix_and_execute():
    inp = get_input()
    length = len(inp)
    acc = 0
    line = 0
    executed = []
    exec_jn = []
    while True:
        executed.append(line)
        ins, val = inp[line].split()
        val = int(val)
        if ins == 'jmp':
            exec_jn.append(line)
            if val < 0 and (line + val) in executed:
                break
            line += val
        else:
            if ins == 'acc':
                acc += val
            else:
                exec_jn.append(line)
            line += 1
    exec_jn.reverse()
    for jn in exec_jn:
        while executed[len(executed) - 1] != jn:
            acc -= int(inp[executed.pop()].split()[1])
        line = jn
        exec_sim = executed.copy()
        acc_sim = acc
        cont = True
        ins, val = inp[jn].split()
        val = int(val)
        if ins == 'nop':
            if val < 0 and (line + val) in executed:
                cont = False
            line += val
        else:
            line += 1
        while cont:
            exec_sim.append(line)
            ins, val = inp[line].split()
            val = int(val)
            if ins == 'jmp':
                if val < 0 and (line + val) in exec_sim:
                    cont = False
                line += val
            else:
                if ins == 'acc':
                    acc_sim += val
                line += 1
            if line >= length:
                return acc_sim
        executed.remove(jn)


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = run_until_repeat()
    elif i == '2':
        ans = fix_and_execute()
    print(ans)
