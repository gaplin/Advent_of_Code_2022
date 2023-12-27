input = open("input/input.txt", "r").read().splitlines()

sums = []
current_value = 0
for line in input:
    if line == '':
        sums.append(current_value)
        current_value = 0
    else:
        current_value += int(line)

sorted_sums = sorted(sums, reverse=True)

print(sorted_sums[0])