import numpy as np
from copy import deepcopy

file = open("14/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

rock_map = [[i for i in l] for l in lines]

def print_map(rock_map):
    for l in rock_map:
        print(''.join(l))


def do_cycle(rock_map):
    new_rock_map = rock_map
    # Move north
    for i in range(len(rock_map[0])):
        next_static_rock = 0
        for j,l in enumerate(rock_map):
            if l[i] == '#':
                next_static_rock = j+1
            elif l[i] == 'O':
                new_rock_map[j][i] = '.'
                new_rock_map[next_static_rock][i] = 'O'
                next_static_rock += 1
    # Move west (left)
    for i in range(len(rock_map)):
        next_static_rock = 0
        for j,l in enumerate(rock_map[i]):
            if l == '#':
                next_static_rock = j+1
            elif l == 'O':
                new_rock_map[i][j] = '.'
                new_rock_map[i][next_static_rock] = 'O'
                next_static_rock += 1
    # Move south
    for i in range(len(rock_map[0])):
        next_static_rock = len(rock_map)-1
        for j in range(len(rock_map)-1,-1,-1):
            if rock_map[j][i] == '#':
                next_static_rock = j-1
            elif rock_map[j][i] == 'O':
                new_rock_map[j][i] = '.'
                new_rock_map[next_static_rock][i] = 'O'
                next_static_rock -= 1
    # print_map(new_rock_map)
    # print()
    # Move right
    for i in range(len(rock_map)):
        next_static_rock = len(rock_map[0])-1
        for j in range(len(rock_map[0])-1,-1,-1):
            if rock_map[i][j] == '#':
                next_static_rock = j-1
            elif rock_map[i][j] == 'O':
                new_rock_map[i][j] = '.'
                new_rock_map[i][next_static_rock] = 'O'
                next_static_rock -= 1
    # print_map(new_rock_map)
    # print()
    return new_rock_map

def compare_maps(rock_map,rock_map2):
    return all((all(rock_map[i][j] == rock_map2[i][j] for j in range(len(rock_map[0]))) for i in range(len(rock_map))))

def calculate_support_beams(rock_map):
    tot = 0
    for y,l in enumerate(rock_map):
        for x,c in enumerate(l):
            if c == 'O':
                tot += len(rock_map) - y
    return tot

last_maps = []
for i in range(200):

    rock_map = do_cycle(rock_map)
    # print_map(rock_map)
    found_cycle = False
    for j,m in enumerate(last_maps):
        if compare_maps(m,rock_map):
            found_cycle = True
            print(i,j)
            last_map_index = (1000000000-j) % (i - j)
            print([calculate_support_beams(z) for z in last_maps])
            print(last_map_index)
            print(calculate_support_beams(last_maps[j+last_map_index-1]))
            break
    last_rock_map = deepcopy(rock_map)
    last_maps.append(last_rock_map)
    if found_cycle: break

        