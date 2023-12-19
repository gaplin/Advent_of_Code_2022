input = open('input2.txt').read().splitlines()

nodes = {}
my_node = 'humn'
operations = {'*': lambda x, y : x * y, '/': lambda x, y : x / y, '+': lambda x, y : x + y, '-': lambda x, y : x - y }
values = {}
humn_on_the_way = {}
for line in input:
    node, children = line.split(':')
    values[node] = 0
    humn_on_the_way[node] = [False, False]
    children = children.strip().split(' ')
    if len(children) == 1:
        nodes[node] = [int(children[0])]
    else:
        nodes[node] = children

def dfs(node_id, my_node):
    my_node_found = False
    if node_id == my_node:
        my_node_found = True
    node = nodes[node_id]
    if len(node) == 1:
        values[node_id] = node[0]
        return my_node_found
    
    my_node_on_left = dfs(node[0], my_node)
    my_node_on_right = dfs(node[2], my_node)
    if my_node_on_left == True:
        humn_on_the_way[node_id][0] = True
        my_node_found = True
    elif my_node_on_right == True:
        humn_on_the_way[node_id][1] = True
        my_node_found = True
    operand = node[1]

    values[node_id] = operations[operand](values[node[0]], values[node[2]])
    return my_node_found

def missing_value_dfs(node_id, value_to_get, my_node):
    values[node_id] = value_to_get
    node = nodes[node_id]
    if len(node) == 1:
        return
    
    left_value = values[node[0]]
    right_value = values[node[2]]
    operand = node[1]

    if humn_on_the_way[node_id][0]:
        if operand == '+':
            missing_value_dfs(node[0], value_to_get - right_value, my_node)
        elif operand == '-':
            missing_value_dfs(node[0], value_to_get + right_value, my_node)
        elif operand == '*':
            missing_value_dfs(node[0], value_to_get / right_value, my_node)
        else:
            missing_value_dfs(node[0], value_to_get * right_value, my_node)
    else:
        if operand == '+':
            missing_value_dfs(node[2], value_to_get - left_value, my_node)
        elif operand == '-':
            missing_value_dfs(node[2], left_value - value_to_get, my_node)
        elif operand == '*':
            missing_value_dfs(node[2], value_to_get / left_value, my_node)
        else:
            missing_value_dfs(node[2], left_value / value_to_get, my_node)

dfs('root', my_node)
root = nodes['root']
left_value = values[root[0]]
right_value = values[root[2]]
if humn_on_the_way['root'][0]:
    missing_value_dfs(root[0], right_value, my_node)
else:
    missing_value_dfs(root[2], left_value, my_node)

print(values[my_node])