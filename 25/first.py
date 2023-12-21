from functools import reduce

def to_snafu(num):
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        mod = num % 5
        num //= 5
        char = ''
        if mod <= 2:
            char = str(mod)
        elif mod == 3:
            char = '='
            num += 1
        else:
            char = '-'
            num += 1
        result = char + result
    return result

def from_snafu(num):
    result = 0
    pow = 1
    for char in num[::-1]:
        if char == '0' or char == '1' or char == '2':
            result += pow * int(char)
        elif char == '-':
            result -= pow
        else:
            result -= 2 * pow
        pow *= 5
    return result

input = open('input2.txt').read().splitlines()

int_sum = reduce(int.__add__, map(from_snafu, input))
snafu_sum = to_snafu(int_sum)

print(snafu_sum)