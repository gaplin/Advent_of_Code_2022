import re
from queue import Queue
from functools import lru_cache

input = open('input_2.txt', 'r').read().splitlines()

rates = {}
G = {}
for line in input:
    valves = re.findall('[A-Z]{2}', line)
    rate = list(map(int, re.findall('\d+', line)))
    rates[valves[0]] = int(rate[0])
    G[valves[0]] = valves[1:]

G_compacted = {}
masks = {}

for valve in G:
    if rates[valve] == 0 and valve != 'AA':
        continue
    if valve != 'AA':
        masks[valve] = 1 << len(masks)
    G_compacted[valve] = []
    visited = set()
    q = Queue()
    q.put((valve, 1))
    visited.add(valve)
    while q.empty() == False:
        u, dist = q.get()
        if u != valve and rates[u] > 0:
            G_compacted[valve].append((u, dist))
        
        for v in G[u]:
            if v not in visited:
                q.put((v, dist + 1))
                visited.add(v)

@lru_cache
def max_flow_rate(u, time_left, opened_valves):
    result = 0

    for v, distance in G_compacted[u]:
        mask = masks[v]
        remaining_time = time_left - distance
        if remaining_time <= 0 or (opened_valves & mask) > 0:
            continue 
        
        flow_increase = remaining_time * rates[v]
        result = max(result, flow_increase + max_flow_rate(v, remaining_time, opened_valves | mask))

    return result

num_of_possibilites = (1 << len(masks)) - 1
result = 0
for i in range(1, (num_of_possibilites // 2) + 1):
    result = max(result, max_flow_rate('AA', 26, i) + max_flow_rate('AA', 26, num_of_possibilites ^ i))

print(result)