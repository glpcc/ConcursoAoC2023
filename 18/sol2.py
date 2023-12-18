import numpy as np
from dataclasses import dataclass
from cProfile import Profile
from pstats import SortKey, Stats
import math

file = open("18/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

corners = []
min_x = math.inf
max_x = -math.inf
min_y = math.inf
max_y = -math.inf

current_x = 0
current_y = 0

dir_sums = {'L': (0,-1),'U': (-1,0),'R': (0,1),'D': (1,0)}
dirs = ['R','D','L','U']
for l in lines:
    _, _, color = l.split(' ')
    num = int(color[2:-2],16)
    d = dirs[int(color[-2])]
    # d, num, color = l.split(' ')
    # num = int(num)
    print(d,num)
    oldx = current_x
    oldy = current_y
    current_x += dir_sums[d][1]*num
    current_y += dir_sums[d][0]*num
    min_x = min(current_x,min_x)
    max_x = max(current_x,max_x)
    min_y = min(current_y,min_y)
    max_y = max(current_y,max_y)
    if d == 'D':
        corners.append((oldy,oldx,current_y,current_x))
    elif d == 'U':
        corners.append((current_y,current_x,oldy,oldx))
print(len(corners))


sorted_x_corners = sorted(corners,key= lambda k: k[1])
sorted_y_corners = sorted(((y,x,y2,x2,i) for i,(y,x,y2,x2) in enumerate(sorted_x_corners)),key= lambda k: k[0])
# print(corners)
# print([(y/max_y,x/max_x,y2/max_y,x2/max_x) for y,x,y2,x2 in corners])
# print(sorted_y_corners)
# print(sorted_x_corners)
# Fill the first list of points for the flood algorithm 
inside_points = 0
print(max_x,min_x,max_y,min_y)
for current_y in range(min_y,max_y+1):
    if current_y % 1000000 == 0:
        print(current_y)
    x_indices = []
    for y,x,y2,x2,i in sorted_y_corners:
        if y > current_y:
            break
        if current_y <= y2:
            x_indices.append(i)
    #print(x_indices)
    if len(x_indices) <= 1:
        continue
    x_indices = sorted(x_indices)
    lines_crossed = 0
    prev_outside = True
    sum_next_barrier = True
    ignore_next = False
    for j,indx in enumerate(x_indices[:-1]):
        # print(current_y,lines_crossed)
        next_indx = x_indices[j+1]
        if ignore_next:
            lines_crossed += 1 if sum_next_barrier else 0
            sum_next_barrier = True
            ignore_next = False
        elif sorted_x_corners[indx][2] == current_y and sorted_x_corners[indx][2] == sorted_x_corners[next_indx][0] :
            lines_crossed += 1 if prev_outside else 0
            sum_next_barrier = not prev_outside
            ignore_next = True
        elif sorted_x_corners[indx][0] == current_y and sorted_x_corners[indx][0] == sorted_x_corners[next_indx][2]:
            lines_crossed += 1 if prev_outside else 0
            sum_next_barrier = not prev_outside
            ignore_next = True
        elif sorted_x_corners[indx][0] == current_y and sorted_x_corners[indx][0] == sorted_x_corners[next_indx][0]:
            lines_crossed += 1 if prev_outside else 0
            sum_next_barrier = prev_outside
            ignore_next = True
        elif sorted_x_corners[indx][2] == current_y and sorted_x_corners[indx][2] == sorted_x_corners[next_indx][2]:
            lines_crossed += 1 if prev_outside else 0
            sum_next_barrier = prev_outside
            ignore_next = True
        else:
            lines_crossed += 1 if sum_next_barrier else 0
            sum_next_barrier = True
        if lines_crossed%2 == 1:
            # print(current_y,sorted_x_corners[next_indx][1] - sorted_x_corners[indx][1]+ (1 if prev_outside else 0),sorted_x_corners[next_indx],sorted_x_corners[indx])
            inside_points += sorted_x_corners[next_indx][1] - sorted_x_corners[indx][1] + (1 if prev_outside else 0)
            prev_outside = False
        else:
            prev_outside = True
print(inside_points)