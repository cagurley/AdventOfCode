def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_total_output_joltage_2():
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


def get_total_output_joltage_12():
    total = 0
    for bank in get_input():
        joltage = ""
        start = 0
        offset = 11
        while offset > -1:
            for i in range(9, 0, -1):
                index = bank[start:len(bank)-offset].find(str(i))
                if index > -1:
                    joltage += str(i)
                    start += index + 1
                    offset -= 1
                    break
        total += int(joltage)
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_output_joltage_2()
    elif ipt == '2':
        ans = get_total_output_joltage_12()
    print(ans)
