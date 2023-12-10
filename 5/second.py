import re

input = open("input/input.txt", "r").read().splitlines()

stacks = [list(stack) for stack in input[:9]]
moves = [re.findall('[0-9]+', line) for line in input[10:]]


for move in moves:
    quantity = int(move[0])
    source = int(move[1]) - 1
    target = int(move[2]) - 1
    popped_entries = []
    for _ in range(quantity):
        popped_entries.append(stacks[source].pop())
    for value in reversed(popped_entries):
            stacks[target].append(value)

for stack in stacks:
    print(stack[-1], end='')