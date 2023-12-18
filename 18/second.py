from queue import Queue

input = open('input2.txt', 'r').read().splitlines()
n = 30
grid = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

for line in input:
    nums = list(map(lambda x : int(x) + 1, line.split(',')))
    grid[nums[0]][nums[1]][nums[2]] = 1

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
visited = set()
q = Queue()
q.put((0, 0, 0))
visited.add((0, 0, 0))
result = 0

while q.empty() == False:
    x, y, z = q.get()

    for dx, dy, dz in directions:
        new_x = x + dx
        new_y = y + dy
        new_z = z + dz
        if new_x < 0 or new_y < 0 or new_z < 0 or new_x >= n or new_y >= n or new_z >= n or (new_x, new_y, new_z) in visited:
            continue
        if grid[new_x][new_y][new_z] == 1:
            result +=1
            continue
        visited.add((new_x, new_y, new_z))
        q.put((new_x, new_y, new_z))

print(result)