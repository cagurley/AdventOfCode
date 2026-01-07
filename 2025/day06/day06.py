def get_input():
    with open('input.txt') as file:
        inp = [line.split() for line in file]
    return inp[:-1], inp[-1]


def get_answer_total():
    terms, ops = get_input()
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


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_answer_total()
    elif ipt == '2':
        ans = None
    print(ans)
