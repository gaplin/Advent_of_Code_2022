import re

input = open('input/input.txt', 'r').read().splitlines()

data = []
beacons = set()
not_beacons_candidates = set()

for line in input:
    nums = tuple(map(int, re.findall('[0-9-]+', line)))
    data.append(nums)
    beacons.add((nums[2], nums[3]))

limit = 2000000

for entry in data:
    beacon_distance = abs(entry[2] - entry[0]) + abs(entry[3] - entry[1])
    x = entry[0]
    y = entry[1]

    distance_to_limit = abs(y - limit)
    i = 0
    while i + distance_to_limit <= beacon_distance:
        not_beacons_candidates.add((x + i, limit))
        not_beacons_candidates.add((x - i, limit))
        i += 1

print(len(not_beacons_candidates - beacons))