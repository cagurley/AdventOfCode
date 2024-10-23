import math
import re


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    return inp


def get_point_total():
    inp = get_input()
    points = 0
    for line in inp:
        winning, given = line.split(': ')[1].split(' | ')
        winning = re.findall(r'\d+', winning)
        given = re.findall(r'\d+', given)
        win_count = 0
        for num in given:
            if num in winning:
                win_count += 1
        if win_count > 0:
            points += int(math.pow(2, win_count-1))
    return points


def get_instance_count():
    inp = get_input()
    cards = []
    for line in inp:
        winning, given = line.split(': ')[1].split(' | ')
        winning = re.findall(r'\d+', winning)
        given = re.findall(r'\d+', given)
        win_count = 0
        for num in given:
            if num in winning:
                win_count += 1
        cards.append([1, win_count])

    card_count = 0
    for i, card in enumerate(cards):
        card_count += card[0]
        if card[1] > 0:
            for n in range(i+1, card[1]+i+1):
                cards[n][0] += card[0]
    return card_count


if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_point_total()
    elif ipt == '2':
        ans = get_instance_count()
    print(ans)
