input = open("input/input.txt", "r").read().splitlines()

n = len(input)
m = len(input[0])

def scenic_score(i, ii):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 1
    for direction in directions:
        y = i
        x = ii
        distance = 0

        while True:
            y += direction[0]
            x += direction[1]
            if x < 0 or x >= m or y < 0 or y >= n:
                break
            distance += 1
            if input[y][x] >= input[i][ii]:
                break
        if distance > 0:
            result *= distance
            
    return result

result = 0
for i in range(n):
    for ii in range(m):
        result = max(result, scenic_score(i, ii))

print(result)