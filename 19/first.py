import re
from math import ceil

input = open('input2.txt').read().splitlines()

blueprints = []
maxs = []

for line in input:
    nums = tuple(map(int, re.findall('\d+', line)))
    new_maxs = [0, 0, 0]
    robots = []
    robots.append((nums[1], 0, 0))
    robots.append((nums[2], 0, 0))
    robots.append((nums[3], nums[4], 0))
    robots.append((nums[5], 0, nums[6]))
    blueprints.append(robots)
    for robot in robots:
        for i in range(3):
            new_maxs[i] = max(new_maxs[i], robot[i])
    maxs.append(new_maxs)

def geodes_count(blueprint_idx, remaining_time, resources, robots, cache):
    key = (remaining_time, resources, robots)
    if key in cache:
        return cache[key]
    result = resources[3] + robots[3] * remaining_time
    if remaining_time <= 1:
        cache[key] = result
        return result

    blueprint = blueprints[blueprint_idx]
    for idx, robot in enumerate(blueprint):
        if idx != 3 and robots[idx] >= maxs[blueprint_idx][idx]:
            continue
        waiting_time = 0
        for i in range(3):
            if robot[i] == 0:
                continue
            if robots[i] == 0:
                waiting_time = remaining_time
                break
            waiting_time = max(waiting_time, ceil((robot[i] - resources[i]) / robots[i]))

        if waiting_time + 1 >= remaining_time:
            continue

        resources_lst = list(resources)
        robots_lst = list(robots)

        for i in range(4):
            resources_lst[i] += (waiting_time + 1) * robots[i]
        for i in range(3):
            resources_lst[i] -= robot[i]
        
        robots_lst[idx] += 1
        result = max(result, geodes_count(blueprint_idx, remaining_time - waiting_time - 1, tuple(resources_lst), tuple(robots_lst), cache))
    
    cache[key] = result
    return result

result = 0
for idx, blueprint in enumerate(blueprints):
    geodes = geodes_count(idx, 24, (0, 0, 0, 0), (1, 0, 0, 0), {})
    result += (idx + 1) * geodes

print(result)