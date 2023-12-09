input = open("input/input.txt", "r").read().splitlines()

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

winning_moves = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

losing_moves = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

sum = 0
for line in input:
    moves = line.split(' ')
    opponent = moves[0]
    outcome = moves[1]

    my_move = ''
    if outcome == 'X':
        my_move = losing_moves[opponent]
    elif outcome == 'Y':
        my_move = opponent
        sum += 3
    else:
        my_move = winning_moves[opponent]
        sum += 6
    sum += scores[my_move]

print(sum)