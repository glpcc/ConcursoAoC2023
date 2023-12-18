import numpy as np
from dataclasses import dataclass
from cProfile import Profile
from pstats import SortKey, Stats
import math

file = open("18/input3.txt", "r")

lines = [i.strip() for i in file.readlines()]

trench_pos = set()
min_x = math.inf
max_x = -math.inf
min_y = math.inf
max_y = -math.inf

current_x = 0
current_y = 0

dir_sums = {'L': (0,-1),'U': (-1,0),'R': (0,1),'D': (1,0)}
for l in lines:
    d, num, _ = l.split(' ')
    num = int(num)
    for i in range(num):
        current_x += dir_sums[d][1]
        current_y += dir_sums[d][0]
        min_x = min(current_x,min_x)
        max_x = max(current_x,max_x)
        min_y = min(current_y,min_y)
        max_y = max(current_y,max_y)
        trench_pos.add((current_y,current_x))

def print_map():
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            print('#' if (y,x) in trench_pos else '.',end='')
        print()

print_map()
print(len(trench_pos))
# Fill the first list of points for the flood algorithm 
print(max_x,min_x,max_y,min_y)
point_list = []
for x in range(min_x,max_x+1):
    if (min_y,x) not in trench_pos:
        point_list.append((min_y,x))
    if (max_y,x) not in trench_pos:
        point_list.append((max_y,x))

for y in range(min_y,max_y+1):
    if (y,min_x) not in trench_pos:
        point_list.append((y,min_x))
    if (y,max_x) not in trench_pos:
        point_list.append((y,max_x))   
print(len(point_list))

# Implement the flod algorithm
visited_pos = set(point_list)
while len(point_list) > 0:
    new_point_list = []
    for y,x in point_list:
        for d in dir_sums:
            new_pos = (y+dir_sums[d][0],x+dir_sums[d][1])
            if max_x > new_pos[1] > min_x and max_y > new_pos[0] > min_y and new_pos not in trench_pos and new_pos not in visited_pos:
                new_point_list.append(new_pos)
                visited_pos.add(new_pos)
    point_list = new_point_list

print(len(visited_pos))
print(abs(max_x-min_x))
print((abs(max_x-min_x+1)*abs(max_y-min_y+1)) - len(visited_pos))