import re

input = open("input/input.txt", "r").read().splitlines()

stacks = [list(stack) for stack in input[:9]]
moves = [re.findall('[0-9]+', line) for line in input[10:]]


for move in moves:
    quantity = int(move[0])
    source = int(move[1]) - 1
    target = int(move[2]) - 1
    for _ in range(quantity):
        popped = stacks[source].pop()
        stacks[target].append(popped)

for stack in stacks:
    print(stack[-1], end='')