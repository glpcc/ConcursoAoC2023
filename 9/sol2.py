import numpy as np

file = open("9/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

tot = 0
for line in lines:
    numbers = np.array([int(i) for i in line.split(' ')])
    first_numers = [numbers[0]]
    while numbers.max() != numbers.min():
        numbers = numbers[1:] - numbers[:-1]
        first_numers.append(numbers[0])
    first_pred = 0
    for n in first_numers[::-1]:
        first_pred = n - first_pred
    tot += first_pred

print(tot)