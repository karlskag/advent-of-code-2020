with open('input3.txt') as f:
    content = f.readlines()
input_list = [[x.strip()] for x in content]

movements = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # [dx, dy]
total_trees = 0

for dx, dy in movements:      
    x = 0
    num_trees = 0
    slopes = iter(input_list)
    for row in slopes:
        data = list(row[0])
        sym = data[x % len(data)]
        if sym == '#': num_trees += 1
        x += dx
        for _ in range(dy - 1):  # extra traversals of y above 1
            next(slopes, None)
    if total_trees == 0 or num_trees == 0: total_trees += num_trees  # first traversal
    else: total_trees *= num_trees 

print(total_trees)
