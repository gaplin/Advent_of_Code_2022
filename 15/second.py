import re

input = open('input/input.txt', 'r').read().splitlines()

data = []

for line in input:
    nums = tuple(map(int, re.findall('[0-9-]+', line)))
    data.append(nums)

limit = 4000000

for current_line in range(0, limit + 1):
    intervals = []
    for entry in data:
        beacon_distance = abs(entry[2] - entry[0]) + abs(entry[3] - entry[1])
        x = entry[0]
        y = entry[1]

        distance_to_limit = abs(y - current_line)
        if distance_to_limit > beacon_distance:
            continue
        
        r = beacon_distance - distance_to_limit
        intervals.append((x - r, x + r))

    intervals.sort()
    merged_intervals = []
    for l, h in intervals:
        if len(merged_intervals) == 0:
            merged_intervals.append([l, h])
            continue

        last_l, last_h = merged_intervals[-1]
        if l > last_h + 1:
            merged_intervals.append([l, h])
            continue

        merged_intervals[-1][1] = max(last_h, h)

    if len(merged_intervals) > 1:
        print(current_line + (merged_intervals[0][1] + 1) * 4000000)
        exit()

raise Exception()