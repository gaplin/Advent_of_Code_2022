input = open("input/input.txt", "r").read().splitlines()

sum = 0
for line in input:
    partlength = len(line) // 2
    firstPart = {}
    secondPart = {}
    for char in line[:partlength]:
        if char in firstPart:
            firstPart[char] += 1
        else :
            firstPart[char] = 1

    for char in line[partlength:]:
        if char in secondPart:
            secondPart[char] += 1
        else :
            secondPart[char] = 1

    for char in firstPart.keys():
        if char in secondPart:
            if char.islower():
                sum += ord(char) - ord('a') + 1
            else:
                sum += ord(char) - ord('A') + 27

print(sum)