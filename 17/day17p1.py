from functools import reduce

jets = list(map(lambda x : 1 if x == '>' else -1, open('input2.txt', 'r').read()))

rocks = [
    [
        ['#', '#', '#', '#']
    ],
    [
        ['.', '#', '.'],
        ['#', '#', '#'],
        ['.', '#', '.']
    ],
    [
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['.', '.', '#']
    ],
    [
        ['#'],
        ['#'],
        ['#'],
        ['#']
    ],
    [
        ['#', '#'],
        ['#', '#']
    ]
    ]

taken_positions = set()
for i in range(7):
    taken_positions.add((i, 0))

rocks_in_place = 0
n = len(jets)
ctr = 0
h = 0
limit = 2022
while rocks_in_place < limit:
    for rock in rocks:
        starting_point = (2, h + 4)
        cords = []
        for i in range(len(rock)):
            for ii in range(len(rock[0])):
                if rock[i][ii] != '.':
                    cords.append([ii + starting_point[0], i + starting_point[1]])
        cords_len = len(cords)
        while True:
            jet_move = jets[ctr]
            ctr = (ctr + 1) % n
            roll_back_jet = False
            for i in range(cords_len):
                cords[i][0] += jet_move
                if roll_back_jet == False and (cords[i][0] > 6 or cords[i][0] < 0 or tuple(cords[i]) in taken_positions):
                    roll_back_jet = True
            if roll_back_jet:
                for i in range(cords_len):
                    cords[i][0] -= jet_move
            rollback_move = False
            for i in range(cords_len):
                cords[i][1] -= 1
                if rollback_move == False and tuple(cords[i]) in taken_positions:
                    rollback_move = True
            if rollback_move:
                for i in range(cords_len):
                    cords[i][1] += 1
                    taken_positions.add(tuple(cords[i]))
                rocks_in_place += 1
                break
        h = max(h, reduce(max, [x[1] for x in cords]))
        if rocks_in_place == limit:
            break
print(h)