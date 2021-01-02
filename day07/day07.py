import re


def get_parents():
    valid = {}
    current = {}
    remaining = {}
    pat = r'\d+ (\w+ \w+)'
    with open('input.txt') as file:
        for line in file.read().splitlines():
            key, text = line.split(' bags contain ')
            val = set(re.findall(pat, text))
            if 'shiny gold' in val:
                valid.update({key: val})
            else:
                remaining.update({key: val})
    previous = set(valid.keys())
    while previous:
        for key in list(remaining):
            val = remaining[key]
            if set.intersection(previous, val):
                current.update({key: val})
                del remaining[key]
        valid.update(current)
        previous.clear()
        previous.update(current.keys())
        current.clear()
    return len(valid)


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = -1
    if i == '1':
        ans = get_parents()
    elif i == '2':
        ans = None
    print(ans)
