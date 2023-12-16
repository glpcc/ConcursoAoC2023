import numpy as np

file = open("14/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

static_rocks = set()
movable_rocks = set()

for i in range(len(lines[0])):
    next_static_rock = 0
    for j,l in enumerate(lines):
        if l[i] == '#':
            static_rocks.add((j,i))
            next_static_rock = j+1
        elif l[i] == 'O':
            movable_rocks.add((next_static_rock,i))
            next_static_rock += 1

def print_map(height,width):
    for i in range(height):
        for j in range(width):
            if (i,j) in movable_rocks:
                print('O',end='')
            elif (i,j) in static_rocks:
                print('#',end='')
            else:
                print('.',end='')
        print()

# print_map(len(lines),len(lines[0]))
tot = 0
for y,x in movable_rocks:
    tot += len(lines) - y

print(tot)