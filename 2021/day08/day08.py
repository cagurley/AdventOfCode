DIGITS = {
    '0': set(['a', 'b', 'c', 'e', 'f', 'g']),
    '1': set(['c', 'f']),
    '2': set(['a', 'c', 'd', 'e', 'g']),
    '3': set(['a', 'c', 'd', 'f', 'g']),
    '4': set(['b', 'c', 'd', 'f']),
    '5': set(['a', 'b', 'd', 'f', 'g']),
    '6': set(['a', 'b', 'd', 'e', 'f', 'g']),
    '7': set(['a', 'c', 'f']),
    '8': set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    '9': set(['a', 'b', 'c', 'd', 'f', 'g'])
}


def get_input():
    inp = []
    with open('input.txt') as file:
        for line in file.read().splitlines():
            line = line.split(' | ')
            for i, p in enumerate(line):
                line[i] = [set(_) for _ in p.split()]
            inp.append(line)
    return inp


def count_1478():
    inp = get_input()
    cnt = 0
    for disp in inp:
        for _ in disp[1]:
            if len(_) in (2, 3, 4, 7):
                cnt += 1
    return cnt


def get_sum():
    inp = get_input()
    sum = 0
    for disp in inp:
        # Determine mapping
        mapp = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None
        }
        digits = {
            2: None,
            3: None,
            4: None,
            5: [],
            6: [],
            7: None
        }
        for digit in disp[0]:
            num = len(digit)
            if 4 < num < 7:
                digits[num].append(digit)
            else:
                digits[num] = digit
        a = (digits[3] - digits[2]).pop()
        mapp[a] = 'a'
        comp = digits[4].copy()
        comp.add(a)
        for digit in digits[5]:
            diff = digit - comp
            if len(diff) == 1:
                val = diff.pop()
                mapp[val] = 'g'
                comp.add(val)
                break
        for digit in digits[5]:
            diff = digit - comp
            if len(diff) == 1:
                val = diff.pop()
                mapp[val] = 'e'
                comp.add(val)
                break
        comp -= digits[4]
        res = []
        for digit in digits[6]:
            diff = digit - comp
            if len(diff) == 3:
                res.append(digit)
        res = res[0] ^ res[1]
        f = (digits[2] - res).pop()
        mapp[f] = 'f'
        mapp[(res - digits[2]).pop()] = 'd'
        mapp[(digits[2] & res).pop()] = 'c'
        res.add(f)
        mapp[(digits[4] - res).pop()] = 'b'

        # Determine and add output
        out = []
        for digit in disp[1]:
            trans = set()
            for seg in digit:
                trans.add(mapp[seg])
            for k, v in DIGITS.items():
                if trans == v:
                    out.append(k)
                    break
        sum += int(''.join(out))
    return sum


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = count_1478()
    elif ipt == '2':
        ans = get_sum()
    print(ans)
