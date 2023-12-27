from functools import reduce

input = open('input2.txt').read().splitlines()
n = len(input) - 2
m = reduce(max, map(len, input[:-2]))
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

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
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
        i, ii = (position[0] + direction[0], position[1] + direction[1])
        di, dii = direction 
        if i == -1 and 50 <= ii < 100:
            i = 150 + (ii - 50)
            ii = 0
            di, dii = (0, 1)
        elif i == -1 and 100 <= ii < 150:
            i = 199
            ii -= 100
        elif ii == 150 and 0 <= i < 50:
            i = 149 - i
            ii = 99
            di, dii = (0, -1)
        elif i == 50 and 100 <= ii < 150:
            i = 50 + (ii - 100)
            ii = 99
            di, dii = (0, -1)
        elif ii == 100 and 50 <= i < 100:
            ii = 100 + (i - 50)
            i = 49
            di, dii = (-1, 0)
        elif ii == 100 and 100 <= i < 150:
            i = 49 - (i - 100)
            ii = 149
            di, dii = (0, -1)
        elif i == 150 and 50 <= ii < 100:
            i = 150 + (ii - 50)
            ii = 49
            di, dii = (0, -1)
        elif ii == 50 and 150 <= i < 200:
            ii = 50 + (i - 150)
            i = 149
            di, dii = (-1, 0)
        elif i == 200 and 0 <= ii < 50:
            ii += 100 
            i = 0
            di, dii = (1, 0)
        elif ii == -1 and 150 <= i < 200:
            ii = 50 + (i - 150)
            i = 0
            di, dii = (1, 0)
        elif ii == -1 and 100 <= i < 150:
            i = 49 - (i - 100)
            ii = 50
            di, dii = (0, 1)
        elif i == 99 and 0 <= ii < 50:
            i = ii + 50
            ii = 50
            di, dii = (0, 1)
        elif ii == 49 and 50 <= i < 100:
            ii = i - 50
            i = 100
            di, dii = (1, 0)
        elif ii == 49 and 0 <= i < 50:
            i = 149 - i
            ii = 0
            di, dii = (0, 1)
        if grid[i][ii] == '#':
            break
        position = (i, ii)
        direction = (di, dii)
        
direction_points = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + direction_points[direction])