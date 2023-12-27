input = open("input/input.txt", "r").read().splitlines()

sum = 0
for idx, line in enumerate(input):
    ranges = line.split(',')
    first_range = [eval(i) for i in ranges[0].split('-')]
    second_range = [eval(i) for i in ranges[1].split('-')]

    if (first_range[0] >= second_range[0] and first_range[1] <= second_range[1]) \
        or (second_range[0] >= first_range[0] and second_range[1] <= first_range[1]):
        sum += 1

print(sum)