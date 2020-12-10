import itertools as it
import time

with open('input10.txt') as f:
    content = f.readlines()
input_list = [int(x) for x in content]
input_list.sort()

def solve_a():
    # d3 init 1 because of device adapter 
    j_min, d1, d3 = 0, 0, 1 
    for jolt in input_list:
        diff = jolt - j_min
        j_min = jolt
        if diff == 1: d1 += 1
        elif diff == 3: d3 += 1 
    return d1 * d3


def count_paths(nodes, index, length, graph):   
    if index == length - 1: return 1
    elif index in graph: return graph[index] # paths to win
    
    _self = nodes[index]
    n, n2, n3 = index + 1, index + 2, index + 3 
    d1 = nodes[n] - _self
    d2, d3 = 4, 4
    
    if d1 < 4: 
        graph[index] = count_paths(nodes, n, length, graph)  
    if n2 <= length - 1 and nodes[n2] - _self < 4:
        graph[index] += count_paths(nodes, n2, length, graph)
    if n3 <= length - 1 and nodes[n3] - _self < 4:
        graph[index] += count_paths(nodes, n3, length, graph)

    return graph[index]

def solve_b():
    list = [0] + input_list + [(input_list[-1] + 3)]
    return count_paths(list, 0, len(list), {})

print('Part 1: ', solve_a())

start = time.time()
print('Part 2:', solve_b())
end = time.time()
# print(end - start) ----------->  0.0001399517059326172       :)
