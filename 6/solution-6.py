import functools as ft

with open('input6.txt') as f:
    content = f.read()

# Part 1: Sum all set lengths (set contains all answered questions without duplicates)
input_list_a = [set(x.replace('\n', '')) for x in content.split('\n\n')]
_sum = ft.reduce(lambda acc, set: acc + len(set), input_list_a, 0)

print('Part 1: ', _sum)


# Part 2: Make each person in groups answers a set. Find intersection in group and sum with all other groups
input_list_b = [x.split('\n') for x in content.split('\n\n')]

list_of_sets = []
for group in input_list_b:
    group_answer_sets = []
    for one_person_answers in group: 
        group_answer_sets.append(set(one_person_answers))
    list_of_sets.append(group_answer_sets)

sum_of_intersections = 0
for group_answers in list_of_sets:
    # Intersection of n sets
    # https://blog.finxter.com/how-to-intersect-multiple-sets-in-python/#:~:text=To%20intersect%20multiple%20sets%2C%20stored,unique%20collection%20of%20unordered%20elements.
    sum_of_intersections += len(group_answers[0].intersection(*group_answers))

print('Part 2: ', sum_of_intersections)