with open('input2.txt') as f:
    content = f.readlines()
inputs = [x.strip().split(' ') for x in content]

validPws = 0

# a
# for limits, letter, pw in inputs:
#     min = limits.split('-')[0]
#     max = limits.split('-')[-1]
#     _letter = letter[0]
#     occ = pw.count(_letter)
#     if occ >= int(min) and occ <= int(max): validPws += 1

#b
for limits, letter, pw in inputs:
    i1 = limits.split('-')[0]
    i2 = limits.split('-')[-1]
    _letter = letter[0]
    
    if (pw[int(i1) - 1] == _letter) is not (pw[int(i2) - 1] == _letter): validPws += 1

print(validPws)


    
