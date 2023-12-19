input = open('input2.txt').read().splitlines()

nodes = []
numbers = list(map(int, input))
n = len(numbers)

decryption_key = 811589153
zero = []
for num in numbers:
    node = [num * decryption_key, [], []]
    if num == 0:
        zero = node
    nodes.append(node)

for i in range(n):
    nodes[i][1] = nodes[(i - 1) % n]
    nodes[i][2] = nodes[(i + 1) % n]

for _ in range(10):
    for node in nodes:
        move = node[0]
        if node == 0:
            continue
        movement = abs(node[0]) % (n - 1)
        current = node
        if node[0] < 0:
            for _ in range(movement):
                previous = current[1]
                previous[1][2] = current
                current[1] = previous[1]
                previous[2] = current[2]
                current[2][1] = previous
                previous[1] = current
                current[2] = previous
        else:
            for _ in range(movement):
                next = current[2]
                next[2][1] = current
                current[2] = next[2]
                next[1] = current[1]
                current[1][2] = next
                next[2] = current
                current[1] = next

result = 0
current = zero
for _ in range(3):
    for _ in range(1000):
        current = current[2]
    result += current[0]

print(result)