input = open("input/input.txt", "r").read().splitlines()

def increment_cycle():
    global cycle
    global result
    cycle += 1
    if cycle % 40 == 20:
        result += X * cycle
    return

cycle = 0
X = 1
result = 0
for line in input:
    if cycle > 220:
        break
    if line[0] == 'n':
        increment_cycle()
    else:
        value = int(line.split(' ')[1])
        increment_cycle()
        increment_cycle()
        X += value

print(result)