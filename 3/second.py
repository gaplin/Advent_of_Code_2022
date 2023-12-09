input = open("input/input.txt", "r").read().splitlines()

sum = 0
for idx in range(0, len(input), 3):
    first_line = input[idx]
    second_line = input[idx + 1]
    third_line = input[idx + 2]

    all_items = {}

    for char in first_line:
        if char not in all_items:
            all_items[char] = 1
    
    for char in second_line:
        if char in all_items:
            all_items[char] = 2
    
    for char in third_line:
        if char in all_items and all_items[char] == 2:
            if char.islower():
                sum += ord(char) - ord('a') + 1
            else:
                sum += ord(char) - ord('A') + 27
            all_items[char] = 3

print(sum)