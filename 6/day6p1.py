input = open("input/input.txt", "r").read()

for i in range(3, len(input)):
    chars = set()
    for j in range(i - 3, i + 1):
        chars.add(input[j])
    if len(chars) == 4:
        print(i + 1)
        break
