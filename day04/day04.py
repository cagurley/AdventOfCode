import re


def get_valid(simple=True):
    if not simple:
        RULES = {
            'byr': re.compile(r'^19[2-9]\d|200[0-2]$'),
            'iyr': re.compile(r'^20(1\d|20)$'),
            'eyr': re.compile(r'^20(2\d|30)$'),
            'hgt': re.compile(r'^1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in$'),
            'hcl': re.compile(r'^#[\da-f]{6}$'),
            'ecl': re.compile(r'^amb|blu|[bg]rn|gry|hzl|oth$'),
            'pid': re.compile(r'^\d{9}$')
        }
    valid = 0
    with open('input.txt') as file:
        inp = file.read().splitlines()
    inp.append('')
    record = ''
    for line in inp:
        if len(line) == 0:
            if simple:
                if len(re.findall(r'(?!cid)([a-z]{3}):', record)) == 7:
                    valid += 1
            else:
                fields = re.findall(r'(?!cid)([a-z]{3}):(\S*)', record)
                if len(fields) == 7:
                    v = True
                    d = {}
                    d.update(fields)
                    for key, val in RULES.items():
                        if not re.match(val, d[key]):
                            v = False
                            break
                    if v:
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
        ans = get_valid(False)
    print(ans)
