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


def get_children():
    def calc_num(kb):
        if bags[kb]['num'] is None:
            tb = 0
            for ik, iv in bags[kb]['children'].items():
                tb += (iv * calc_num(ik) + iv)
            bags[kb]['num'] = tb
        return bags[kb]['num']

    bags = {}
    pat = r'(\d+) (\w+ \w+)'
    with open('input.txt') as file:
        for line in file.read().splitlines():
            key, text = line.split(' bags contain ')
            vals = re.findall(pat, text)
            children = {}
            for val in vals:
                children.update({val[1]: int(val[0])})
            data = {'children': children}
            if children:
                data['num'] = None
            else:
                data['num'] = 0
            bags.update({key: data})
    return calc_num('shiny gold')


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = -1
    if i == '1':
        ans = get_parents()
    elif i == '2':
        ans = get_children()
    print(ans)
