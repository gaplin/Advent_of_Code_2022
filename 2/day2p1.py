input = open("input/input.txt", "r").read().splitlines()

scores = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

sum = 0
for line in input:
    moves = line.split(' ')
    opponent = moves[0]
    me = moves[1]

    if scores[me] == scores[opponent]:
        sum += 3
    else:
        if (me == 'X' and opponent == 'C') or (me == 'Y' and opponent == 'A') or (me == 'Z' and opponent == 'B'):
            sum += 6
    sum += scores[me]

print(sum)