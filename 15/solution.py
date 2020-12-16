with open('input.txt') as f:
    content = f.read()

input_list = content.split(',')
mem = {}
latest_num = int(input_list[-1])
latest_first = True

# create initial map
for i in range (1, len(input_list) + 1):
    mem[int(input_list[i-1])] = i

# change range end for part 1 or 2 answ
for i in range(len(input_list) + 1, 30000001):
    if latest_first:
        latest_num = 0
        latest_first = False
    else:
        next_num = (i - 1) - mem[latest_num]
        mem[latest_num] = i - 1
        if next_num in mem:
            latest_first = False
        else: 
            latest_first = True
            mem[next_num] = i
        latest_num = next_num

print('Answer: ', latest_num)

# Turn 1: The 1st number spoken is a starting number, 0.
# Turn 2: The 2nd number spoken is a starting number, 3.
# Turn 3: The 3rd number spoken is a starting number, 6.
# Turn 4: Now, consider the last number spoken, 6. Since that was the first time the number had been spoken, the 4th number spoken is 0.
# Turn 5: Next, again consider the last number spoken, 0. Since it had been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, 4) and the turn number of the time it was most recently spoken before then (turn 1). Thus, the 5th number spoken is 4 - 1, 3.
# Turn 6: The last number spoken, 3 had also been spoken before, most recently on turns 5 and 2. So, the 6th number spoken is 5 - 2, 3.
# Turn 7: Since 3 was just spoken twice in a row, and the last two turns are 1 turn apart, the 7th number spoken is 1.
# Turn 8: Since 1 is new, the 8th number spoken is 0.
# Turn 9: 0 was last spoken on turns 8 and 4, so the 9th number spoken is the difference between them, 4.
# Turn 10: 4 is new, so the 10th number spoken is 0.
