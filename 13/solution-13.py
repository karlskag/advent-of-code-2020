import itertools as it

with open('input13.txt') as f:
    content = f.readlines()
input_list = [x.strip() for x in content]

def solve_a(minute, bus_intervals):
    valid_intervals = it.filterfalse(lambda interval: interval == 'x', bus_intervals)
    shortest_interval = 1000
    best_id = None
    for _id in valid_intervals:
        for i in it.count(start=1):
            mult = i * int(_id)
            if mult > minute:
                wait = mult - minute
                if wait < shortest_interval:
                    best_id = int(_id) 
                    shortest_interval = wait
                break 

    return shortest_interval * best_id

def solve_b(intervals):
    valid_intervals = list(map(int, it.filterfalse(lambda interval: interval == 'x', intervals)))
    # TODO
    

print('Part 1:', solve_a(int(input_list[0]), input_list[1].split(',')))
print('Part 2:', solve_b(input_list[1].split(',')))