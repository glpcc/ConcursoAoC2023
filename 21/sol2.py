# This script is just for getting some data to do analysis on

import re
from matplotlib import pyplot as plt
import numpy as np
import pickle
file = open("21/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

rock_map = lines

current_positions = set()
for y,l in enumerate(rock_map):
    for x,c in enumerate(l):
        if c == 'S':
            current_positions.add((y,x))
            break
print(current_positions)

def print_map(current_positions):
    for y,l in enumerate(rock_map):
        for x,c in enumerate(l):
            print('O' if (y,x) in current_positions else c,end='')
        print()

days = 600
directions = [(-1,0),(1,0),(0,1),(0,-1)]
len_directions = []
for d in range(days):
    new_current_positions = set()
    for y,x in current_positions:
        for dy,dx in directions:
            if rock_map[(y+dy)%len(rock_map)][(x+dx)%len(rock_map[0])] != '#':
                new_current_positions.add((y+dy,x+dx))

    current_positions = new_current_positions
    print(len(current_positions),d)
    len_directions.append(len(current_positions))
    #print_map(current_positions)
# print(len(current_positions))
len_directions = np.array(len_directions)
with open('num_steps_arr2.pkl','wb') as f:
    pickle.dump(len_directions, f)
plt.plot(len_directions[1:] - len_directions[:-1])
plt.show()