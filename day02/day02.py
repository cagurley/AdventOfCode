import re


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
print(valid)
