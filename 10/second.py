input = open("input/input.txt", "r").read().splitlines()

def increment_cycle():
    global cycle
    global pixels
    global X
    pixel_position = (cycle // 40, cycle % 40)
    cycle += 1
    if abs(X - pixel_position[1]) <= 1:
        pixels[pixel_position[0]][pixel_position[1]] = '#'

pixels = [['.' for _ in range(40)] for _ in range(6)]
cycle = 0
X = 1
for line in input:
    if cycle > 240:
        break
    if line[0] == 'n':
        increment_cycle()
    else:
        value = int(line.split(' ')[1])
        increment_cycle()
        increment_cycle()
        X += value

for row in pixels:
    print(''.join(row))