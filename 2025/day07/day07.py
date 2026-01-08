from collections import deque


def get_input():
    with open('input.txt') as file:
        inp = deque(file.read().splitlines())
    return inp


def get_total_splits():
    layers = get_input()
    beams = [layers.popleft().find("S")]
    splits = 0
    stop = len(layers) - 1
    for i, layer in enumerate(layers):
        if i < stop:
            new_beams = []
            for n, beam in enumerate(beams):
                if layers[i+1][beam] == '^':
                    if new_beams and new_beams[-1] == beam - 1:
                        new_beams.append(beam + 1)
                    else:
                        new_beams.extend((beam-1, beam+1))
                    splits += 1
                else:
                    if not(new_beams and new_beams[-1] == beam):
                        new_beams.append(beam)
            beams = new_beams
    return splits



if __name__ == '__main__':
    ipt = input("Part 1 or part 2?  ")
    ans = None
    if ipt == '1':
        ans = get_total_splits()
    elif ipt == '2':
        ans = None
    print(ans)
