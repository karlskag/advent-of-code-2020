with open('input12.txt') as f:
    content = f.readlines()
input_list = [x.strip() for x in content]

def solve_a(commands):
    pos = [0, 0]
    # x, y directions 
    east, south, west, north = [1, 0], [0, -1], [-1, 0], [0, 1]
    turns = [east, south, west, north]
    movements = {
        'N': north,
        'S': south,
        'E': east,
        'W': west
    }
    current_turn_i = 0
    for cmd in commands:
        direction = cmd[0]
        quantity = int(cmd[1:])
        if direction in movements.keys():
            pos = [c + (d * quantity) for c, d in zip(pos, movements[direction])]
        elif direction == 'F':
            pos = [c + (d * quantity) for c, d in zip(pos, turns[int(current_turn_i % 4)])]
        else:
            n_turns = quantity/90 % 4
            if direction == 'R': current_turn_i += n_turns
            else: current_turn_i -= n_turns

    return abs(pos[0]) + abs(pos[1]) 

def solve_b(commands):
    pos = [0, 0]
    waypoint_rel_pos = [10, 1]
    # x, y directions 
    east, south, west, north = [1, 0], [0, -1], [-1, 0], [0, 1]
    turns = [east, south, west, north]
    movements = {
        'N': north,
        'S': south,
        'E': east,
        'W': west
    }
    current_turn_i = 0
    for cmd in commands:
        direction = cmd[0]
        quantity = int(cmd[1:])
        if direction in movements.keys():
            waypoint_rel_pos = [c + (d * quantity) for c, d in zip(waypoint_rel_pos, movements[direction])]
        elif direction == 'F':
            pos = [c + (d * quantity) for c, d in zip(pos, waypoint_rel_pos)]
        else:
            n_turns = int(quantity/90 % 4)
            _position = [waypoint_rel_pos[0], waypoint_rel_pos[1]]
            if direction == 'R': 
                for i in range(n_turns):
                    _position = [_position[1], -_position[0]]
                waypoint_rel_pos = _position
            else: 
                for i in range(n_turns):
                    _position = [-_position[1], _position[0]]
                waypoint_rel_pos = _position

    return abs(pos[0]) + abs(pos[1]) 


print('Part 1: ', solve_a(input_list))
print('Part 2: ', solve_b(input_list))