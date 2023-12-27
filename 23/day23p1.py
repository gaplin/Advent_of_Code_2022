def handle_round(elves, all_directions, moving_directions, neighbours):
    proposed_positions = {}
    for i, ii in elves:
        any_elf = False
        for di, dii in all_directions:
            new_i, new_ii = i + di, ii + dii
            if (new_i, new_ii) in elves:
                any_elf = True
                break
        if any_elf == False:
            continue
        for di, dii in moving_directions:
            all_empty = True
            for ni, nii in neighbours[(di, dii)]:
                new_i = i + ni
                new_ii = ii + nii
                if (new_i, new_ii) in elves:
                    all_empty = False
                    break
            if all_empty == False:
                continue
            new_i = i + di
            new_ii = ii + dii
            key = (new_i, new_ii)
            if key in proposed_positions:
                proposed_positions[key].append((i, ii))
            else:
                proposed_positions[key] = [(i, ii)]
            break   
    for target, sources in proposed_positions.items():
        if len(sources) == 1:
            elves.remove(sources[0])
            elves.add(target)
    
    moving_directions.append(moving_directions.pop(0))

elves = set()
input = open('input2.txt').read().splitlines()
for i in range(len(input)):
    for ii in range(len(input[i])):
        if input[i][ii] == '#':
            elves.add((i, ii))
    
moving_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
all_directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
neighbours = {
    (-1, 0): ((-1, 0), (-1, -1), (-1, 1)), 
    (1, 0): ((1, 0), (1, -1), (1, 1)),
    (0, 1): ((0, 1), (1, 1), (-1, 1)),
    (0, -1): ((0, -1), (1, -1), (-1, -1))
    }

for _ in range(10):
    handle_round(elves, all_directions, moving_directions, neighbours)

top = 99999999999
bot = -999999999
left = 99999999
right = -99999999
for i, ii in elves:
    top = min(top, i)
    bot = max(bot, i)
    left = min(left, ii)
    right = max(right, ii)

print((bot - top + 1) * (right - left + 1) - len(elves))