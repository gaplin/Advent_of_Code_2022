from functools import cmp_to_key

input = open('input/input.txt', 'r').read().splitlines()
input.append('[[6]]')
input.append('[[2]]')

packets = []
for line in input:
    if line == '':
        continue
    packets.append(eval(line))

def order(A, B):
    if type(A) is int and type(B) is int:
        if A == B:
            return 0
        if A > B:
            return 1
        return -1
    
    if type(A) is list and type(B) is list:
        a_size = len(A)
        b_size = len(B)
        limit = min(a_size, b_size)
        for i in range(limit):
            element_order = order(A[i], B[i])
            if element_order != 0:
                return element_order 
        if a_size == b_size:
            return 0
        if a_size > b_size:
            return 1
        return -1
    
    if type(A) is int:
        return order([A], B)
    
    return order(A, [B])

packets = sorted(packets, key=cmp_to_key(order))
divider_2 = [[2]]
divider_6 = [[6]]
result = (packets.index(divider_2) + 1) * (packets.index(divider_6) + 1)

print(result)