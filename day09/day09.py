from collections import deque


def get_input():
    with open('input.txt') as file:
        inp = file.read().splitlines()
    for index, line in enumerate(inp):
        inp[index] = int(line)
    return inp


def find_corrupted():
    inp = get_input()
    stack = deque(inp[:25])
    inp = inp[25:]
    ordered = list(stack)
    for num in inp:
        ordered.sort()
        left = 0
        right = 24
        while left < right:
            complement = num - ordered[left]
            while right > left and complement < ordered[right]:
                right -= 1
            complement = num - ordered[right]
            while left < right and complement > ordered[left]:
                left += 1
            if complement == ordered[left]:
                break
        if left < right:
            stack.append(num)
            ordered.remove(stack.popleft())
            ordered.append(num)
        else:
            return num


def find_weakness():
    corruption = find_corrupted()
    inp = get_input()
    stack = deque()
    sum = 0
    index = 0
    while sum != corruption:
        while sum < corruption:
            num = inp[index]
            stack.append(num)
            sum += num
            index += 1
        while sum > corruption:
            sum -= stack.popleft()
    return max(stack) + min(stack)


if __name__ == '__main__':
    i = input("Part 1 or part 2?  ")
    ans = None
    if i == '1':
        ans = find_corrupted()
    elif i == '2':
        ans = find_weakness()
    print(ans)
