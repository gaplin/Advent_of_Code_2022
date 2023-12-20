from functools import reduce

input = open('input2.txt').read().splitlines()
n = len(input) - 2
m = reduce(max, map(len, input))
grid = []
for line in input[:-2]:
    m_line = len(line)
    if m_line < m:
        line += ' ' * (m - m_line)
    grid.append(line)
movement = input[-1]

steps = []
num = 0
for symbol in movement:
    if symbol == 'L' or symbol == 'R':
        if num > 0:
            steps.append(num)
        steps.append(symbol)
        num = 0
    else:
        num = num * 10 + int(symbol)
if num > 0:
    steps.append(num)    

teleports = {}
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n) :
    leftmost = -1
    rightmost = -1
    for ii in range(m):
        if grid[i][ii] != ' ':
            leftmost = ii
            rightmost = ii
            break
    for ii in reversed(range(m)):
        if grid[i][ii] != ' ':
            rightmost = ii
            break
    if leftmost == -1:
        continue
    teleports[((i, leftmost - 1), (0, -1))] = (i, rightmost)
    teleports[((i, rightmost + 1), (0, 1))] = (i, leftmost)

for i in range(m):
    topmost = -1
    botmost = -1
    for ii in range(n):
        if grid[ii][i] != ' ':
            topmost = ii
            botmost = ii
            break
    for ii in reversed(range(n)):
        if grid[ii][i] != ' ':
            botmost = ii
            break
    if topmost == -1:
        continue
    teleports[((topmost - 1, i), (-1, 0))] = (botmost, i)
    teleports[((botmost + 1, i), (1, 0))] = (topmost, i)

starting_position = (-1, -1)
for i in range(n):
    for ii in range(m):
        if grid[i][ii] == '.':
            starting_position = (i, ii)
            break
    if starting_position[0] != -1:
        break

position = starting_position
direction = (0, 1)

for move in steps:
    if move == 'L':
        direction = (-direction[1], direction[0])
        continue
    if move == 'R':
        direction = (direction[1], -direction[0])
        continue
    for i in range(move):
        position_candidate = (position[0] + direction[0], position[1] + direction[1])
        if (position_candidate, direction) in teleports:
            position_candidate = teleports[(position_candidate, direction)]
        if grid[position_candidate[0]][position_candidate[1]] == '#':
            break
        position = position_candidate
        
direction_points = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + direction_points[direction])