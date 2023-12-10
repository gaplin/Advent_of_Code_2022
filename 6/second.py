input = open("input/input.txt", "r").read()

for i in range(13, len(input)):
    chars = set()
    for j in range(i - 13, i + 1):
        chars.add(input[j])
    if len(chars) == 14:
        print(i + 1)
        break
