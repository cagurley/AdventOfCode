import re


def valid_by_count():
    valid = 0
    with open('input.txt') as file:
        for line in file.readlines():
            lower, upper, letter, password = re.search(r'^(\d+)-(\d+) (\w): (\w+)$', line).groups()
            lower = int(lower)
            upper = int(upper)
            count = 0
            for l in password:
                if l == letter:
                    count += 1
                    if count > upper:
                        break
            if lower <= count <= upper:
                valid += 1
    return valid


def valid_by_pos():
    valid = 0
    with open('input.txt') as file:
        for line in file.readlines():
            first, second, letter, password = re.search(r'^(\d+)-(\d+) (\w): (\w+)$', line).groups()
            first = int(first) - 1
            second = int(second) - 1
            v = False
            if password[first] == letter:
                v = not v
            if password[second] == letter:
                v = not v
            if v:
                valid += 1
    return valid


if __name__ == '__main__':
    i = input('Answer part 1 or 2?  ')
    ans = -1
    if i == '1':
        ans = valid_by_count()
    elif i == '2':
        ans = valid_by_pos()
    print(ans)
