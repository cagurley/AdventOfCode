def get_ranges():
    with open('input.txt') as file:
        inp = file.read().strip()
    ranges = [v.split("-") for v in inp.split(",")]
    return ranges


def get_invalid_sum():
    invalid_sum = 0
    for start, end in get_ranges():
        if len(start) % 2 > 0:
            start = "1" + "0" * len(start)
        else:
            mid = int(len(start) / 2)
            if int(start[:mid]) < int(start[mid:]):
                start = str(int(start[:mid]) + 1) * 2
        while True:
            mid = int(len(start)/2)
            half = start[:mid]
            start = start[:mid] * 2
            if int(start) > int(end):
                break
            invalid_sum += int(start)
            start = str(int(half) + 1) * 2
    return invalid_sum

if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_invalid_sum()
    elif ipt == '2':
        ans = None
    print(ans)
