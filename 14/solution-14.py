import re
import itertools as it
import copy

with open('input14.txt') as f:
    content = f.readlines()
input_list = [x.strip() for x in content]

def solve_a(commands):
    mem = {}
    mask = None
    for cmd in commands:
        if 'mask' in cmd:
            mask = list(cmd.split(' ')[-1])
        else:
            num = int(cmd.split(' ')[-1])
            slot = int(re.findall(r'\d+', cmd)[0])
            bits = '{:036b}'.format(num)
            mask_res = list(bits)
            for i, bit in enumerate(mask):
                if bit == 'X': continue
                else: mask_res[i] = bit
            mem[slot] = mask_res
    _sum = 0
    for n in mem.values():
        string_ints = [str(int) for int in n]
        s = "".join(string_ints)   
        _sum += int(s, 2)
    return _sum

# Create possible combinations of 1 & 0 based on number of X in mask, 
# and then use them to create all possible memory-adresses                
def solve_b(commands):
    mem = {}
    mask = None
    for cmd in commands:
        if 'mask' in cmd:
            mask = list(cmd.split(' ')[-1])
        else:
            slot = int(re.findall(r'\d+', cmd)[0])
            bits = '{:036b}'.format(slot)
            num = int(cmd.split(' ')[-1])
            num_x = mask.count('X')
            combinations = list(it.product([1, 0], repeat=num_x))
            all_mem_slots = []
            for i in range(len(combinations)):
                all_mem_slots.append(list(bits))
            nx = -1
            for i, bit in enumerate(mask):
                if bit == 'X':
                    nx += 1                
                    for _i, ms in enumerate(all_mem_slots):
                        ms[i] = str(combinations[_i][nx])
                elif bit == '1':
                    for memslot in all_mem_slots: memslot[i] = bit
                # ignore 0's
            for slotname in all_mem_slots:
                string_slot = [str(int) for int in slotname]
                s = "".join(string_slot)
                mem[s] = num               
    _sum = 0
    for n in mem.values():
        _sum += n
    return _sum
    
# print('Part 1: ', solve_a(input_list))
print('Part 2: ', solve_b(input_list))