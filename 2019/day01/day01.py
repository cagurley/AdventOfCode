def get_input():
    with open('input.txt') as file:
        inp = [int(num) for num in file.read().splitlines()]
    return inp


def get_fuel_sum():
    inp = get_input()
    total = 0
    for num in inp:
        total += num//3 - 2
    return total


def get_series_fuel_sum():
    inp = get_input()
    total = 0
    for num in inp:
        step = num//3 - 2
        while step > 0:
            total += step
            step = step//3 - 2
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_fuel_sum()
    elif ipt == '2':
        ans = get_series_fuel_sum()
    print(ans)
