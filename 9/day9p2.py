input = open("input/input.txt", "r").read().splitlines()

snake = [(0, 0) for _ in range(10)]

visited_position = set()
visited_position.add(snake[9])

directions_map = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

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
        snake[0] = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        for i in range(1, 10):
            relative_dir = relative_direction(snake[i], snake[i - 1])
            moved_part = (snake[i][0] + relative_dir[0], snake[i][1] + relative_dir[1])
            if moved_part != snake[i - 1]:
                snake[i] = moved_part
        steps -= 1
        visited_position.add(snake[9])
    
print(len(visited_position))