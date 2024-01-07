import re


WORDS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_digit_sum():
    total = 0
    for line in get_input():
        first = re.search(r'\d', line).group()
        last = re.search(r'(\d)\D*$', line).group(1)
        num = int(f"{first}{last}")
        total += num
    return total


def get_semantic_sum():
    total = 0
    count = 0
    for line in get_input():
        count += 1
        matches = dict()
        dm = re.search(r'\d', line)
        matches[dm.start()] = dm.group()
        for k, v in WORDS.items():
            match = re.search(k, line)
            if match is not None:
                matches[match.start()] = v
        first = matches[min(matches.keys())]
        matches.clear()
        dm = re.search(r'.*(\d)', line)
        matches[dm.end()] = dm.group(1)
        if count == 27:
            count=count
        for k, v in WORDS.items():
            match = re.search(f".*{k}", line)
            if match is not None:
                matches[match.end()] = v
        last = matches[max(matches.keys())]
        total += int(f"{first}{last}")
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_digit_sum()
    elif ipt == '2':
        ans = get_semantic_sum()
    print(ans)
