def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_script_score():
    inp = get_input()
    decode = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    total = 0
    for round in inp:
        sel = round.split()
        total += decode[sel[1]]
        diff = (decode[sel[1]] - decode[sel[0]]) % 3
        if diff == 1:
            total += 6
        elif diff == 0:
            total += 3
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_script_score()
    elif ipt == '2':
        ans = None
    print(ans)
