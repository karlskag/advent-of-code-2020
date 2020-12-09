import itertools as it

with open('input9.txt') as f:
    content = f.readlines()
input_list = [int(x) for x in content]

def solve_a():
    preamble_end = 25
    preamble_start = -1
    for i, num in enumerate(input_list):
        if i <= (preamble_end - 1): continue 
        preamble_start += 1
        preamble_end += 1
        added_permutations = map(lambda p: sum(p), it.permutations(input_list[preamble_start:preamble_end], 2))
        if num not in added_permutations: return num 

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq)))

def solve_b():
    # Find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    err_num = solve_a();
    preamble_size = 2
    while True:
        if preamble_size > 20: return 'Timeout!'
        try: 
            groups = list(chunker(input_list, preamble_size))
            added_groups = map(lambda p: sum(p), groups)
            i = list(added_groups).index(err_num)
            r = list(groups)[i];
            return min(r) + max(r)
        except ValueError: preamble_size += 1

print('Part 1: ', solve_a())
print('Part 2: ', solve_b())