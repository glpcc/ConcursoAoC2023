import numpy as np

file = open("9/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

tot = 0
for line in lines:
    numbers = np.array([int(i) for i in line.split(' ')])
    end_numers = [numbers[-1]]
    while numbers.max() != numbers.min():
        numbers = numbers[1:] - numbers[:-1]
        end_numers.append(numbers[-1])
    tot += sum(end_numers)

print(tot)