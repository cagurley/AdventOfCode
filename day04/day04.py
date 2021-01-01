import re


def get_valid():
    valid = 0
    with open('input.txt') as file:
        inp = file.read().splitlines()
    inp.append('')
    record = ''
    for line in inp:
        if len(line) == 0:
            if len(re.findall(r'(?!cid)([a-z]{3}):', record)) == 7:
                valid += 1
            record = ''
        else:
            record += (' ' + line)
    return valid


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = -1
    if i == '1':
        ans = get_valid()
    elif i == '2':
        ans = None
    print(ans)
