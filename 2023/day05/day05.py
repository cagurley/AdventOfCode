from collections import deque


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_processed_input(as_end=False):
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
                if as_end:
                    vals[2] = vals[1] + vals[2]
                maps[src]["ranges"].append(vals)
                n += 1
    return seeds, maps


def get_lowest_location_number_by_list():
    nums, maps = get_processed_input(True)
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
    # min_location = None
    # for n in range(0, len(ranges), 2):
    sl_map = []
    for r in maps["seed"]["ranges"]:
        sl_map.append([[r[1], r[0]], [r[1]+r[2], r[0]+r[2]]])
    sl_map = sorted(sl_map, key=lambda entry: entry[0][0])
    i = 0
    end = len(sl_map) - 1
    while i < end:
        if sl_map[i][1][0] < sl_map[i+1][0][0]:
            sl_map.append([[sl_map[i][1][0], sl_map[i][1][0]], [sl_map[i+1][0][0], sl_map[i+1][0][0]]])
        i += 1
    sl_map = sorted(sl_map, key=lambda entry: entry[0][1])

    key = maps["seed"]["dest"]
    while key != "location":
        new_map = []
        for r in maps[key]["ranges"]:
            new_map.append([[r[1], r[0]], [r[1]+r[2], r[0]+r[2]]])
        new_map = sorted(new_map, key=lambda entry: entry[0][0])
        i = 0
        end = len(new_map) - 1
        while i < end:
            if new_map[i][1][0] < new_map[i+1][0][0]:
                new_map.append([[new_map[i][1][0], new_map[i][1][0]], [new_map[i+1][0][0], new_map[i+1][0][0]]])
            i += 1
        new_map = sorted(new_map, key=lambda entry: entry[0][0])

        i = 0
        j = 0
        while i < len(new_map):
            while j < len(sl_map) and new_map[i][1][0] >= sl_map[j][1][1]:
                offset = new_map[i][0][1] - new_map[i][0][0]
                sl_map[j][0][1], sl_map[j][1][1] = (offset + sl_map[j][0][1]), (offset + sl_map[j][1][1])
                j += 1
            if j >= len(sl_map):
                break
            if new_map[i][1][0] == sl_map[j][0][1]:
                i += 1
            if sl_map[j][1][1] > new_map[i][1][0]:
                offset = new_map[i][1][0] - sl_map[j][0][1]
                split_map = [sl_map[j].copy(), sl_map[j].copy()]
                split_map[0][1] = [split_map[0][0][0] + offset, split_map[0][0][1] + offset]
                split_map[1][0] = split_map[0][1].copy()
                sl_map[j] = split_map[1]
                sl_map.insert(j, split_map[0])
        bool(1==1)
        key = maps[key]["dest"]

            # if sl_map[j][1][1] <= new_map[i][1][0]:
            #     offset = sl_map[j][0][1] - new_map[j][0][0]
            #     sl_map[j][0][1] = (new_map[i][0][1] + offset), (new_map[i][1][1] + sl_map[j][1][0] - sl_map[j][0][0])
            # for r in maps[key]["ranges"]:
            #     if num >= r[1] and num < r[2]:
            #         num = r[0] + num - r[1]
            #         break
            # key = maps[key]["dest"]
            # if min_location is None or min_location > num:
            #     min_location = num
    return None


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_lowest_location_number_by_list()
    elif ipt == '2':
        ans = get_lowest_location_number_by_range()
    print(ans)
