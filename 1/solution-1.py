with open('input1.txt') as f:
    content = f.readlines()
input_string = [x.strip() for x in content]

array = list(map(int, input_string))
desiredSum = 2020

# b
for idx, num1 in enumerate(array):
    if idx == len(array) - 1: break
    for num2 in array[idx + 1:]:
        for num3 in array[idx + 2:]:
            if num1 + num2 + num3 == desiredSum: print(num1 * num2 * num3)
