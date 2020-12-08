import re

with open('input4.txt') as f:
    content = f.read()
input_list = content.split('\n\n')

nr_valid = 0
for passp in input_list:
    # a
    # nr_matches = re.findall(r"byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:", passp)
    
    #b
    nr_matches = re.findall(r'byr:(19[2-9]\d|200[0-2])|iyr:(201\d|2020)|eyr:(202\d|2030)|hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)|hcl:#([a-f0-9]{6}\b)|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:([0-9]{9}\b)', passp)
    if len(nr_matches) == 7: nr_valid += 1 

print(nr_valid)
