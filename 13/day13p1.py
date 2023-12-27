input = open('input/input.txt', 'r').read().splitlines()

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
        
pairs = []
pair_idx = 0
result = 0
for line in input:
    if line == '':
        continue
    pairs.append(eval(line))

    if len(pairs) == 2:
        pair_idx += 1
        if order(pairs[0], pairs[1]) <= 0:
            result += pair_idx
        pairs = []

print(result)