input = open("input/input.txt", "r").read().splitlines()

visible_tree = [[False for _ in range(len(input[0]))] for _ in range(len(input))]

# left to right
n = len(input)
m = len(input[0])
for i in range(0, n):
    previous_height = '-'
    for ii in range(0, m):
        if input[i][ii] > previous_height:
            visible_tree[i][ii] = True
            previous_height = input[i][ii]

# right to left
for i in range(0, n):
    previous_height = '-'
    for ii in reversed(range(0, m)):
        if input[i][ii] > previous_height:
            visible_tree[i][ii] = True
            previous_height = input[i][ii]


# top to bottom
for i in range(0, m):
    previous_height = '-'
    for ii in range(0, n):
        if input[ii][i] > previous_height:
            visible_tree[ii][i] = True
            previous_height = input[ii][i]

# bottom to top
for i in range(0, m):
    previous_height = '-'
    for ii in reversed(range(0, n)):
        if input[ii][i] > previous_height:
            visible_tree[ii][i] = True
            previous_height = input[ii][i]

result = 0
for row in visible_tree:
    result += row.count(True)

print(result)