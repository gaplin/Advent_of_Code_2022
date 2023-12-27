input = open("input/input.txt", "r").read().splitlines()

sum = 0
for idx, line in enumerate(input):
    ranges = line.split(',')
    first_range = [eval(i) for i in ranges[0].split('-')]
    second_range = [eval(i) for i in ranges[1].split('-')]

    intersection = (max(first_range[0], second_range[0]), min(first_range[1], second_range[1]))
    if intersection[0] <= intersection[1]:
        sum += 1

print(sum)