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
limit = 1000000000000

heights = []
visited_spaces = {}
cycle_start = 0
cycle_length = 0
cycle_found = False
while cycle_found == False:
    for idx, rock in enumerate(rocks):
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
                old_h = h
                differences = tuple(list((cord[0], cord[1] - h, ctr) for cord in cords))
                potential_h = reduce(max, [x[1] for x in cords])
                heights.append(h)
                h = max(h, potential_h)
                if len(taken_positions) > 10:
                    df = sorted(taken_positions, key= lambda x : x[1], reverse=True)[:10]
                    space = tuple((d[1] - old_h, ctr) for d in df)
                    if space in visited_spaces:
                        cycle_found = True
                        cycle_start = visited_spaces[space]
                        cycle_length = rocks_in_place - cycle_start
                        break
                    visited_spaces[space] = (rocks_in_place)
                break
        if cycle_found == True:
            break

cycle_start -= 1
starting_height = heights[cycle_start]
result = heights[cycle_start]
for i in range(cycle_start, len(heights)):
    heights[i] -= starting_height

limit -= cycle_start
result += limit // cycle_length * heights[-1]

limit %= cycle_length
if limit > 0:
    result += heights[cycle_start + limit % cycle_length]

print(result)