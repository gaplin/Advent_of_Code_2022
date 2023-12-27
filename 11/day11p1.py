import re

input = open('input/input.txt', 'r').read().splitlines()
monkeys = []

for line in input:
    if line == '':
        continue

    if line.startswith('M'):
        monkeys.append([])
        continue

    if 'items' in line:
        nums = re.findall('[0-9]+', line)
        monkeys[-1].append([int(x) for x in nums])
        continue

    if 'Operation' in line:
        num = re.findall('[0-9]+', line)
        if len(num) == 0:
            if '+' in line:
                monkeys[-1].append(lambda x : x + x)
            else:
                monkeys[-1].append(lambda x : x * x)
        else:
            num = int(num[0])
            if '+' in line:
                monkeys[-1].append(lambda x, y = num : x + y)
            else:
                monkeys[-1].append(lambda x, y = num : x * y)
        continue

    if 'Test' in line or 'true' in line or 'false' in line:
        num = int(re.findall('[0-9]+', line)[0])
        monkeys[-1].append(num)

inspections = [0 for _ in range(len(monkeys))]

for _ in range(20):
    for idx, monkey in enumerate(monkeys):
        for item in monkey[0]:
            inspections[idx] += 1
            item = monkey[1](item)
            item //= 3
            if item % monkey[2] == 0:
                monkeys[monkey[3]][0].append(item)
            else:
                monkeys[monkey[4]][0].append(item)
        monkey[0] = []
    

inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])