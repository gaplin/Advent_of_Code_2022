input = open('input2.txt').read().splitlines()

nodes = {}
operations = {'*': lambda x, y : x * y, '/': lambda x, y : x / y, '+': lambda x, y : x + y, '-': lambda x, y : x - y }
for line in input:
    node, children = line.split(':')
    children = children.strip().split(' ')
    if len(children) == 1:
        nodes[node] = [int(children[0])]
    else:
        nodes[node] = children

def dfs(node_id):
    node = nodes[node_id]
    if len(node) == 1:
        return node[0]
    
    left_value = dfs(node[0])
    right_value = dfs(node[2])
    operand = node[1]
    return operations[operand](left_value, right_value)

print(dfs('root'))