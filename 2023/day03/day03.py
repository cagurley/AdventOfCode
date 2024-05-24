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



if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_part_sum()
    elif ipt == '2':
        ans = None
    print(ans)
