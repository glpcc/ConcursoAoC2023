import re

file = open("6/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

times = [int(i) for i in re.findall('\d+',lines[0] )]
max_distances = [int(i) for i in re.findall('\d+',lines[1] )]

tot = 1
for i,t in enumerate(times):
    posible_holding_times = 0
    for t_holding in range(t):
        if (t-t_holding)*t_holding > max_distances[i]:
            posible_holding_times += 1
    tot *= posible_holding_times

print(tot)