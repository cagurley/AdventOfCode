def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_possible_sum():
    total = 0
    for line in get_input():
        game, reveals = line.split(': ')
        reveals = reveals.split('; ')
        add_id = True
        for r in reveals:
            for show in r.split(', '):
                num, color = show.split(' ')
                num = int(num)
                if color == 'red' and num > 12:
                    add_id = False
                    break
                elif color == 'green' and num > 13:
                    add_id = False
                    break
                elif color == 'blue' and num > 14:
                    add_id = False
                    break
            if add_id is False:
                break
        if add_id:
            total += int(game.split(' ')[1])
    return total


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_possible_sum()
    elif ipt == '2':
        ans = None
    print(ans)
