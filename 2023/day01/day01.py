import re


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_calibration_sum():
    total = 0
    for line in get_input():
        first = re.search(r'\d', line).group()
        last = re.search(r'(\d)\D*$', line).group(1)
        num = int(f"{first}{last}")
        total += num
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_calibration_sum()
    elif ipt == '2':
        ans = None
    print(ans)
