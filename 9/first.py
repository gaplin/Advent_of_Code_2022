input = open("input/input.txt", "r").read().splitlines()

head = (0, 0)
tail = (0, 0)

visited_position = set()
visited_position.add(tail)

directions_map = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def relative_direction(A, B):
    result = [0, 0]

    if B[0] > A[0]:
        result[0] = 1
    elif B[0] < A[0]:
        result[0] = -1
    
    if B[1] > A[1]:
        result[1] = 1
    elif B[1] < A[1]:
        result[1] = -1

    return result

for line in input:
    dir_steps = line.split(' ')
    direction = directions_map[dir_steps[0]]
    steps = int(dir_steps[1])

    while steps > 0:
        head = (head[0] + direction[0], head[1] + direction[1])
        relative_dir = relative_direction(tail, head)
        moved_tail = (tail[0] + relative_dir[0], tail[1] + relative_dir[1])
        if moved_tail != head:
            tail = moved_tail
        steps -= 1
        visited_position.add(tail)
    
print(len(visited_position))