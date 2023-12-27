from queue import Queue

input = open('input/input.txt', 'r').read().splitlines()

S = (0, 0)
E = (0, 0)
n = len(input)
m = len(input[0])

for i in range(n):
    for ii in range(m):
        if input[i][ii] == 'S':
            input[i] = input[i].replace('S', 'a')
            S = (i, ii)
        elif input[i][ii] == 'E':
            input[i] = input[i].replace('E', 'z')
            E = (i, ii)

q = Queue()
visited = set()
result = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited.add(S)
q.put((S[0], S[1], 0))

while q.empty() == False:
    i, ii, distance = q.get()
    if (i, ii) == E:
        result = distance
        break
    for di, dii in directions:
        new_i = i + di
        new_ii = ii + dii
        if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= m or (new_i, new_ii) in visited \
            or ord(input[new_i][new_ii]) - ord(input[i][ii]) > 1:
            continue
        visited.add((new_i, new_ii))
        q.put((new_i, new_ii, distance + 1))

print(result)