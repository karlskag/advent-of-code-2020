import copy

with open('input8.txt') as f:
    content = f.readlines()
input_list = [x.strip().split(' ') for x in content]

# Part 1
def solve_a(curr_i = 0, value = 0, visited = {}):
    # Avoid mutating dict when called from solve_b
    # I'm getting same result without copying, so probably not needed... 
    _visited = copy.deepcopy(visited)
    while True:
        el = input_list[curr_i]
        cmd, delta = el[0], el[1]
        if curr_i in _visited:
            return ('loop', value)
        
        _visited[curr_i] = True
        if cmd == 'nop':
            curr_i += 1
            if curr_i == len(input_list): return ('term', value)
        elif cmd == 'acc':
            value += int(delta)
            curr_i += 1
            if curr_i == len(input_list): return ('term', value)
        else: #jmp
            curr_i += int(delta)
            if curr_i == len(input_list): return ('term', value)

# Part 2: Use part 1 solver to check if changing the command terminates the program without loop 
def solve_b(curr_i = 0, value = 0, visited = {}):
    while True:
        el = input_list[curr_i]
        cmd, delta = el[0], el[1]
        
        if cmd == 'nop':
            new_i = curr_i + 1
            if new_i == len(input_list): return value
            check = solve_a(curr_i + int(delta), value, visited)
            if check[0] == 'term': return check[1]   
            else: curr_i = new_i
        elif cmd == 'acc':
            value += int(delta)
            curr_i += 1
            if curr_i == len(input_list): return value
        else: #jmp
            new_i = curr_i + int(delta)
            if new_i == len(input_list): return value
            check = solve_a(curr_i + 1, value, visited)
            if check[0] == 'term': return check[1]   
            else: curr_i = new_i

print('Part 1: ', solve_a())
print('Part 2: ', solve_b())