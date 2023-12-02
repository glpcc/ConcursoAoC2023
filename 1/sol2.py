import re

file = open("1/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

new_lines = lines.copy()
digits = {'one':'one1one','two':'two2two','three':'three3three','four':4,'five':'5five','six':6,'seven':'7seven','eight':'eight8eight','nine':'9nine'}

for i in range(len(new_lines)):
    for dig in digits:
        new_lines[i] = new_lines[i].replace(dig,str(digits[dig]))
tot = 0
for i,word in enumerate(new_lines):
    digits = [i for i in word if i.isnumeric()]
    tot += int(digits[0] + digits[-1])
    # print(f'{lines[i]} {word} {int(digits[0] + digits[-1])}')
print(tot)