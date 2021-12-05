class Board:
    def __init__(self):
        self.win = False
        self.tiles = {}
        self.state = [[False for _ in range(5)] for _ in range(5)]

    def check(self, val):
        if val in self.tiles:
            x, y = self.tiles[val]
            self.state[x][y] = True
            for _ in range(5):
                if self.state[_][y] is False:
                    break
                elif _ == 4:
                    self.win = True
            for _ in range(5):
                if self.state[x][_] is False:
                    break
                elif _ == 4:
                    self.win = True
        return self.win

    def calculate_score(self, val):
        sum = 0
        for k, v in self.tiles.items():
            x, y = v
            if self.state[x][y] is False:
                sum += int(k)
        return sum * int(val)


def get_input():
    with open('input.txt') as file:
        calls = file.readline().split(',')
        boards = []
        while file.readline():
            b = file.read(75)
            board = Board()
            for x, line in enumerate(b.splitlines()):
                for y, _ in enumerate(line.split()):
                    board.tiles.update({_: (x, y)})
            boards.append(board)
    return calls, boards


def get_winning_score():
    calls, boards = get_input()
    for c in calls:
        for n, b in enumerate(boards):
            if b.check(c):
                return b.calculate_score(c)
    return None


def get_last_winning_score():
    calls, boards = get_input()
    rem = len(boards)
    for c in calls:
        for n, b in enumerate(boards):
            if b.win is False and b.check(c):
                rem -= 1
                if rem == 0:
                    return b.calculate_score(c)
    return None


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = get_winning_score()
    elif i == '2':
        ans = get_last_winning_score()
    print(ans)
