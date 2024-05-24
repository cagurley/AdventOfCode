def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def is_symbol(char):
    return not char.isdigit() and char != "."


def get_part_sum():
    inp = get_input()
    LINE_COUNT = len(inp)
    LINE_LENGTH = len(inp[0])
    i = 0
    j = 0
    start = None
    end = None
    num = ""
    total = 0
    while i < LINE_COUNT:
        while j <= LINE_LENGTH:
            if j < LINE_LENGTH and inp[i][j].isdigit():
                num += inp[i][j]
                if start is None:
                    start = j
            else:
                if start is not None:
                    end = j - 1
                if num:
                    add = False
                    if i > 0:
                        for n in range(max(0, start-1), min(LINE_LENGTH, end+2)):
                            if is_symbol(inp[i-1][n]):
                                add = True
                                break
                    if not add and start > 0 and is_symbol(inp[i][start-1]):
                        add = True
                    if not add and end < LINE_LENGTH - 1 and is_symbol(inp[i][end+1]):
                        add = True
                    if not add and i < LINE_COUNT - 1:
                        for n in range(max(0, start-1), min(LINE_LENGTH, end+2)):
                            if is_symbol(inp[i+1][n]):
                                add = True
                                break
                    if add:
                        total += int(num)
                    start = None
                    end = None
                    num = ""
            if j == LINE_LENGTH:
                i += 1
                if i >= LINE_COUNT:
                    break
                j = 0
            else:
                j += 1
    return total


def get_gear_sum():
    inp = get_input()
    LINE_COUNT = len(inp)
    LINE_LENGTH = len(inp[0])
    total = 0
    for i, row in enumerate(inp):
        for j, char in enumerate(row):
            if char == "*":
                nums = []
                if i > 0:
                    n = max(0, j-1)
                    while n < min(LINE_LENGTH, j+2):
                        if inp[i-1][n].isdigit():
                            start = n
                            end = n
                            while start > 0:
                                if inp[i-1][start-1].isdigit():
                                    start -= 1
                                else:
                                    break
                            while end < LINE_LENGTH-1:
                                if inp[i-1][end+1].isdigit():
                                    end += 1
                                    n += 1
                                else:
                                    break
                            nums.append(int(inp[i-1][start:end+1]))
                        n += 1
                if j > 0 and inp[i][j-1].isdigit():
                    start = j - 1
                    end = j - 1
                    while start > 0:
                        if inp[i][start-1].isdigit():
                            start -= 1
                        else:
                            break
                    nums.append(int(inp[i][start:end+1]))
                if j < LINE_LENGTH - 1 and inp[i][j+1].isdigit():
                    start = j + 1
                    end = j + 1
                    while end < LINE_LENGTH - 1:
                        if inp[i][end+1].isdigit():
                            end += 1
                        else:
                            break
                    nums.append(int(inp[i][start:end+1]))
                if i < LINE_COUNT - 1:
                    n = max(0, j-1)
                    while n < min(LINE_LENGTH, j+2):
                        if inp[i+1][n].isdigit():
                            start = n
                            end = n
                            while start > 0:
                                if inp[i+1][start-1].isdigit():
                                    start -= 1
                                else:
                                    break
                            while end < LINE_LENGTH-1:
                                if inp[i+1][end+1].isdigit():
                                    end += 1
                                    n += 1
                                else:
                                    break
                            nums.append(int(inp[i+1][start:end+1]))
                        n += 1
                if len(nums) == 2:
                    total += nums[0] * nums[1]
    return total



if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_part_sum()
    elif ipt == '2':
        ans = get_gear_sum()
    print(ans)
