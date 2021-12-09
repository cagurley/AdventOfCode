def get_input():
    with open('input.txt') as file:
        inp = file.read().strip().split(',')
    return [int(_) for _ in inp]


def get_const_align_cost():
    inp = get_input()
    inp.sort()
    crabs = len(inp)
    mid = crabs//2
    pos = inp[mid]
    if crabs % 2 == 0:
        pos = (inp[mid-1] + pos) // 2
    fuel = 0
    for _ in inp:
        fuel += abs(_ - pos)
    return fuel


def get_lin_align_cost():
    inp = get_input()
    inp.sort()
    crabs = len(inp)
    fuel = 0
    mean = 0
    for _ in inp:
        mean += _
    mean = round(mean / crabs)
    inc = -1
    inp = [_ - mean for _ in inp]
    new = [_ + inc for _ in inp]
    diff = 0
    for idx in range(crabs):
        val = abs(inp[idx])
        nval = abs(new[idx])
        if nval > val:
            diff += nval
        else:
            diff -= val
    if diff < 0:
        inp = new
    else:
        inc = 1
    while True:
        new = [_ + inc for _ in inp]
        diff = 0
        for idx in range(crabs):
            val = abs(inp[idx])
            nval = abs(new[idx])
            if nval > val:
                diff += nval
            else:
                diff -= val
        if diff < 0:
            inp = new
        else:
            break
    for _ in inp:
        _ = abs(_)
        fuel += (_ * (_ + 1)) // 2
    return fuel


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_const_align_cost()
    elif i == '2':
        ans = get_lin_align_cost()
    print(ans)
