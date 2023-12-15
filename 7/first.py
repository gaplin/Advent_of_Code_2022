input = open("input/input.txt", "r").read().splitlines()

directories = {}
current_directory = '/'

sizes = {}

for line in input:
    if line[0] == '$':
        if line[2] == 'l':
            continue
        step = line[5:]
        if step.startswith('/'):
            current_directory = step
        elif step == '..':
            slash_idx = len(current_directory) - 1
            while slash_idx > 1 and current_directory[slash_idx] != '/':
                slash_idx -= 1
            current_directory = current_directory[:slash_idx]
        else:
            if current_directory != '/':
                current_directory += '/'
            current_directory += step
    else:
        values = line.split(' ')
        if values[0] == 'dir':
            if current_directory == '/':
                values[1] = '/' + values[1]
            else:
                values[1] = current_directory + '/' + values[1]
        if current_directory not in directories:
            directories[current_directory] = []
        if values not in directories[current_directory]:
            directories[current_directory].append(tuple(values))

def calc_size(directory):
    result = 0
    for entry in directories[directory]:
        if entry[0] != 'dir':
            result += int(entry[0])
        else:
            result += calc_size(entry[1])

    sizes[directory] = result
    return result

calc_size('/')

result = 0
for directory, size in sizes.items():
    if size <= 100000:
        result += size

print(result)