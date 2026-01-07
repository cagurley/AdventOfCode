def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp[:-1], inp[-1]


def get_horizontal_total():
    terms, ops = get_input()
    terms = [line.split() for line in terms]
    ops = ops.split()
    total = 0
    i = 0
    length = len(ops)
    while i < length:
        if ops[i] == "+":
            answer = 0
            for line in terms:
                answer += int(line[i])
            total += answer
        else:
            answer = 1
            for line in terms:
                answer *= int(line[i])
            total += answer
        i += 1
    return total


def get_vertical_total():
    lines, ops = get_input()
    total = 0
    stops = []
    for i, c in enumerate(ops):
        if c != " ":
            stops.append(i)

    i = len(ops) - 1
    stops.reverse()
    for stop in stops:
        terms = []
        while i >= stop:
            term = ""
            for line in lines:
                term += line[i]
            terms.append(int(term))
            i -= 1
        if ops[stop] == "+":
            answer = 0
            for term in terms:
                answer += term
            total += answer
        else:
            answer = 1
            for term in terms:
                answer *= term
            total += answer
        i -= 1
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_horizontal_total()
    elif ipt == '2':
        ans = get_vertical_total()
    print(ans)
