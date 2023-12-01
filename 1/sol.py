file = open("1/input.txt", "r")

lines = list(file.readlines())

tot = 0
for word in lines:
    digits = [i for i in word if i.isnumeric()]
    tot += int(digits[0] + digits[-1])

print(tot)