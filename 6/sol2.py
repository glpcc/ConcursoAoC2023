import re
import math

file = open("6/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

time = int(''.join([i for i in re.findall('\d+',lines[0] )]))
max_distance = int(''.join([i for i in re.findall('\d+',lines[1] )]))
tot = 1

for t_holding in range(time):
    if (time-t_holding)*t_holding > max_distance:
        first_posible_t = t_holding
        break

print(first_posible_t)
# Other posible (much faster) way to solve i found later
print(math.sqrt(time*time - 4*max_distance))
print(time - first_posible_t*2 + 1)