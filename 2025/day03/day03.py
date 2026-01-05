def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_total_output_joltage():
    total = 0
    for bank in get_input():
        for i in range(9, 0, -1):
            index = bank.find(str(i))
            if -1 < index < len(bank) - 1:
                for j in range(9, 0, -1):
                    if bank[index+1:].find(str(j)) > -1:
                        total += int(str(i) + str(j))
                        break
                break
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_output_joltage()
    elif ipt == '2':
        ans = None
    print(ans)
