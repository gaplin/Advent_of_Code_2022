import re

input = open('input/input.txt', 'r').read().splitlines()

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def valid_point(x, y, limit, sensors):
    if x < 0 or x > limit or y < 0 or y > limit:
         return False
    for x2, y2, r in sensors:
        dist = distance(x, y, x2, y2)
        if dist <= r:
            return False
    return True

data = []
for line in input:
    x, y, bx, by = tuple(map(int, re.findall('[0-9-]+', line)))
    data.append((x, y, distance(x, y, bx, by)))

limit = 4000000
for x, y, r in data:
    new_point = (x + r + 1, y)
    if valid_point(new_point[0], new_point[1], limit, data):
        print(new_point[0] * 4000000 + new_point[1])
        break

    point_found = False
    for i in range(1, r + 2):
        new_point = (x + r + 1 - i, y + i)
        if valid_point(new_point[0], new_point[1], limit, data):
            print(new_point[0] * 4000000 + new_point[1])
            point_found = True
            break
        new_point = (x + r + 1 - i, y - i)
        if valid_point(new_point[0], new_point[1], limit, data):
            print(new_point[0] * 4000000 + new_point[1])
            point_found = True
            break
        new_point = (x - r - 1 + i, y + i)
        if valid_point(new_point[0], new_point[1], limit, data):
            print(new_point[0] * 4000000 + new_point[1])
            point_found = True
            break
        new_point = (x - r - 1 + i, y - i)
        if valid_point(new_point[0], new_point[1], limit, data):
            print(new_point[0] * 4000000 + new_point[1])
            point_found = True
            break

    if point_found == True:
        break