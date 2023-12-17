from functools import reduce

input = open('input/input.txt', 'r').read().splitlines()
n = 1000
m = 1000

grid = [['.' for _ in range(m)] for _ in range(n)]

max_y = 0
for line in input:
    cords_lst = list(map(lambda x : x.split(','), line.replace(' ', '').split('->')))
    current_max_y = reduce(max, map(lambda x : int(x[1]), cords_lst))
    max_y = max(max_y, current_max_y)

    for i in range(1, len(cords_lst)):
        previous = (int(cords_lst[i - 1][0]), int(cords_lst[i - 1][1]))
        current = (int(cords_lst[i][0]), int(cords_lst[i][1]))

        x_limit = (min(previous[0], current[0]), max(previous[0], current[0]) + 1)
        y_limit = (min(previous[1], current[1]), max(previous[1], current[1]) + 1)
        for x in range(min(previous[0], current[0]), max(previous[0], current[0]) + 1):
            for y in range(min(previous[1], current[1]), max(previous[1], current[1]) + 1):
                grid[y][x] = '#'

floor = max_y + 2
for ii in range(m):
    grid[floor][ii] = '#'

S = (0, 500)

result = 0
while True:
    y, x = S
    if grid[y][x] != '.':
        break
    
    while True:
        if grid[y + 1][x] == '.':
            y += 1
        elif grid[y + 1][x - 1] == '.':
            y += 1
            x -= 1
        elif grid[y + 1][x + 1] == '.':
            y += 1
            x +=1 
        else:
            grid[y][x] = 'O'
            break
    
    result += 1

print(result)