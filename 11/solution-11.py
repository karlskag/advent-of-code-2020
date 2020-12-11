import copy

with open('input11.txt') as f:
    content = f.readlines()
input_list = [list(x.strip()) for x in content]

def getadjacentseats(list, y, y_max, x, x_max):
    adj = []
    if y != 0:
        adj.append(list[y-1][x]) # above
        if x != 0: adj.append(list[y-1][x-1]) # top left
        if x != x_max: adj.append(list[y-1][x+1]) # top right
    if x != 0: adj.append(list[y][x-1]) # left
    if x != x_max: adj.append(list[y][x+1]) # right
    if y != y_max:
        adj.append(list[y+1][x]) # below
        if x != 0: adj.append(list[y+1][x-1]) # bottom left
        if x != x_max: adj.append(list[y+1][x+1]) # bottom right
    return adj

def getvisibleseats(list, y, y_max, x, x_max):
    matches = ('L', '#')
    l, dul, u, dur, r, ddr, d, ddl = [], [], [], [], [], [], [], []
    # up and diagonally up
    for _y in range(y-1, -1, -1):
        _lx = (x - (y - _y))
        _rx = (x + (y - _y))
        if len(dul + u + dur) == 3: break
        if len(u) == 0 and list[_y][x] in matches: u.append(list[_y][x]) # up
        if len(dul) == 0 and _lx >= 0 and list[_y][_lx] in matches: dul.append(list[_y][_lx]) # top left
        if len(dur) == 0 and _rx <= x_max and list[_y][_rx] in matches: dur.append(list[_y][_rx]) # top right
    # right left
    for _x in range(x-1, -1, -1):
        if len(l) == 1: break
        elif list[y][_x] in matches: l.append(list[y][_x]) # left
    for _x in range(x+1, x_max + 1):
        if len(r) == 1: break
        elif list[y][_x] in matches: r.append(list[y][_x]) # right     
    # down and diagonally down
    for _y in range(y+1, y_max + 1):
        _lx = (x - (_y - y))
        _rx = (x + (_y - y))
        if len(ddl + d + ddr) == 3: break
        if len(d) == 0 and list[_y][x] in matches: d.append(list[_y][x]) # down
        if len(ddl) == 0 and _lx >= 0 and list[_y][_lx] in matches: ddl.append(list[_y][_lx]) # bottom left
        if len(ddr) == 0 and _rx <= x_max and list[_y][_rx] in matches: ddr.append(list[_y][_rx]) # bottom right

    return l + dul + u + dur + r + ddr + d + ddl

def count_occ(list, char):
    occ = 0
    for y in list:
        occ += y.count('#')
    return occ

def reach_equilibrium(prev_seating, flip_min, strategy):
    next_seating = copy.deepcopy(prev_seating)
    x_max = len(prev_seating[0]) - 1
    y_max = len(prev_seating) - 1
    
    for row_i, row in enumerate(prev_seating):
        for seat_i, seat in enumerate(row):
            if seat != '.':                
                adj_seats = strategy(prev_seating, row_i, y_max, seat_i, x_max)
                if seat == '#':
                    if adj_seats.count('#') >= flip_min:
                        next_seating[row_i][seat_i] = 'L'
                elif seat == 'L':
                    if adj_seats.count('#') == 0:
                        next_seating[row_i][seat_i] = '#'
    if next_seating == prev_seating: return count_occ(next_seating, '#')
    else: return reach_equilibrium(next_seating, flip_min, strategy)

def solve_a():
    return reach_equilibrium(input_list, 4, getadjacentseats)

def solve_b():
    return reach_equilibrium(input_list, 5, getvisibleseats)

print('Part 1:', solve_a())
print('Part 2:', solve_b())
