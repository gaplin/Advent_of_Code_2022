input = open('input2.txt', 'r').read().splitlines()
n = 20

grid = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

for line in input:
    nums = list(map(int, line.split(',')))
    grid[nums[0]][nums[1]][nums[2]] = 1

result = 0
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
for i in range(n):
    for ii in range(n):
        for iii in range(n):
            if grid[i][ii][iii] == 1:
                result += 6
                for dx, dy, dz in directions:
                    new_i = i + dx
                    new_ii = ii + dy
                    new_iii = iii + dz
                    if new_i < 0 or new_ii < 0 or new_iii < 0 or new_i >= n or new_ii >= n or new_iii >= n \
                    or grid[new_i][new_ii][new_iii] != 1:
                        continue
                    result -= 1

print(result)