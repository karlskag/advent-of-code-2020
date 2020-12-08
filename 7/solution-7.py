import re
import functools as ft

with open('input7.txt') as f:
    content = f.read()
input_list = content.split('\n')

# Create flat structure of all rules for quick lookup
rule_map = {}
for rule in input_list:
    exp_string = rule.split(' ')
    bag_key = exp_string[0] + exp_string[1]
    rule_map[bag_key] = {}
    contains = re.findall(r'(\d \w+ \w+)', rule)
    for c_rule in contains:
        inner_rules = c_rule.split(' ')
        rule_map[bag_key][inner_rules[1] + inner_rules[2]] = inner_rules[0]

# Part 1: Find all rules containing bag colors recursively and make unique
def findAllUniqueContainers(key, rules, matching_keys = []):
    new_matches = []
    for k, v in rules.items():
        if key in v.keys() : new_matches.append(k)
    if len(new_matches) == 0: return matching_keys
    matching_keys.extend(new_matches)
    [findAllUniqueContainers(nk, rules, matching_keys) for nk in new_matches]
    return set(matching_keys)

# Part 2: Recursively sum all bags and their content
def findContainedSum(key, rules, _sum = 0):
    contained_rules = rules[key]
    if len(contained_rules) == 0: return 0
    return ft.reduce(
        lambda acc, k: acc + (int(contained_rules[k]) + (int(contained_rules[k]) * findContainedSum(k, rules))), 
        contained_rules.keys(), _sum
    )
    # for k, v in contained_items:
    #     _sum += int(v) + (int(v) * findContainedSum(k, rules))
    # return _sum

print('Part 1: ', len(findAllUniqueContainers('shinygold', rule_map)))
print('Part 2: ', findContainedSum('shinygold', rule_map)) # answ: 7867