def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_processed_input():
    data = get_input()
    seeds = [int(v) for v in data[0].split(": ")[1].split()]
    maps = {}
    n = 2
    while n < len(data):
        src, dest = data[n].split()[0].split("-")[::2]
        maps[src] = {"dest": dest, "ranges": []}
        n += 1
        while True:
            if n >= len(data) or not data[n]:
                n += 1
                break
            else:
                vals = [int(v) for v in data[n].split()]
                vals[2] = vals[1] + vals[2]
                maps[src]["ranges"].append(vals)
                n += 1
    return seeds, maps


def get_lowest_location_number_by_list():
    nums, maps = get_processed_input()
    key = "seed"
    while key != "location":
        for i, num in enumerate(nums):
            for r in maps[key]["ranges"]:
                if num >= r[1] and num < r[2]:
                    nums[i] = r[0] + num - r[1]
                    break
        key = maps[key]["dest"]
    return min(nums)


def get_lowest_location_number_by_range():
    ranges, maps = get_processed_input()
    min_location = None
    for n in range(0, len(ranges), 2):
        start, end = ranges[n], ranges[n]+ranges[n+1]
        for num in range(start, end):
            key = "seed"
            while key != "location":
                for r in maps[key]["ranges"]:
                    if num >= r[1] and num < r[2]:
                        num = r[0] + num - r[1]
                        break
                key = maps[key]["dest"]
            if min_location is None or min_location > num:
                min_location = num
    return min_location


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_lowest_location_number_by_list()
    elif ipt == '2':
        ans = get_lowest_location_number_by_range()
    print(ans)
