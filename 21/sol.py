import re
from dataclasses import dataclass
from dataclasses import field
import queue

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
days = 64
directions = [(-1,0),(1,0),(0,1),(0,-1)]
for d in range(days):
    new_current_positions = set()
    for y,x in current_positions:
        for dy,dx in directions:
            if 0 <= y+dy < len(rock_map) and 0 <= x+dx < len(rock_map[0]) and rock_map[y+dy][x+dx] != '#':
                new_current_positions.add((y+dy,x+dx))

    current_positions = new_current_positions
    # print_map(current_positions)
print(len(current_positions))