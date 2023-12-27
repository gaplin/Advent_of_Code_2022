from math import lcm
from queue import Queue

def min_time(source, target, blizzards, directions, lc, n, m, starting_time):
    q = Queue()
    visited = set()
    q.put((source, starting_time))
    visited.add((source, starting_time))

    while q.empty() == False:
        position, time = q.get()
        if position == target:
            return time
        
        time += 1
        for di, dii in directions:
            new_i, new_ii = position[0] + di, position[1] + dii
            new_position = (new_i, new_ii)
            if ((new_i, new_ii), time % lc) in visited:
                continue
            if new_position != source and new_position != target and \
                (new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= m):
                continue
            
            blizzard_collision = False
            if new_position != source and new_position != target:
                for dir, blizzard_set in blizzards.items():
                    rewind_i = (new_i - dir[0] * time) % n
                    rewind_ii = (new_ii - dir[1] * time) % m
                    if (rewind_i, rewind_ii) in blizzard_set:
                        blizzard_collision = True
                        break
            if blizzard_collision == False:
                q.put((new_position, time))
                visited.add((new_position, time % lc))

    raise Exception('no result found')

directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]
blizzards = { (0, 1): set(), (1, 0): set(), (-1, 0): set(), (0, -1): set()}
input = open('input2.txt').read().splitlines()
n = len(input)
m = len(input[0])
for i in range(n):
    for ii in range(m):
        position = (i - 1, ii - 1)
        symbol = input[i][ii]
        if symbol == '>':
            blizzards[(0, 1)].add(position)
        elif symbol == '<':
            blizzards[(0, -1)].add(position)
        elif symbol == '^':
            blizzards[(-1, 0)].add(position)
        elif symbol == 'v':
            blizzards[(1, 0)].add(position)

n -= 2
m -= 2
lc = lcm(n, m)

result = 0
path = ((-1, 0), (n, m - 1), (-1, 0), (n, m - 1))
for i in range(1, 4):
    result += min_time(path[i - 1], path[i], blizzards, directions, lc, n, m, result) - result

print(result)