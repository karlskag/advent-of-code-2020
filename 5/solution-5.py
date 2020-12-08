with open('input5.txt') as f:
    content = f.readlines()
input_list = [[x.strip()] for x in content]

row_ids = []
# Could (should) do this with binary to decimal conversion (F & L = 0, B & R = 1)
# Part 1: Answer is max(row_ids)
for cmd in input_list:
    rows = list(range(128))
    cols = list(range(8))
    cmds = list(cmd[0]) # split string
    for dy in cmds:
        if dy == 'F': rows = rows[:len(rows)//2]
        elif dy == 'B': rows = rows[len(rows)//2:]
        elif dy == 'R': cols = cols[len(cols)//2:]
        elif dy == 'L': cols = cols[:len(cols)//2]
    row_ids.append(rows[0] * 8 + cols[0])

# Part 2 New: 
# A nicer approach below (difference between sum of ids and theorethical sum of min to max ids):
print('Part 2: ', sum(range(min(row_ids), max(row_ids) + 1)) - sum(row_ids))


# Part 2 Old:
# def diff(first, second):
#         second = set(second)
#         return [item for item in first if item not in second]
# 
# all_ids = list(range(max(row_ids) + 1))
# empty_seats = diff(all_ids, row_ids) 
# Could take above diff and find number (id) where num + and - 1 exists in row_ids (would be 717)
