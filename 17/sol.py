import numpy as np
from dataclasses import dataclass
from cProfile import Profile
from pstats import SortKey, Stats

file = open("17/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

heat_loss_map = [[int(i) for i in l] for l in lines]

def calculate_heuristic(y,x):
   return 2*(len(heat_loss_map[0]) - x) + 2*(len(heat_loss_map) - y)

# Las direcciones son 0 izq, 1 up , 2 right, 3 down
dir_sums = [(0,-1),(-1,0),(0,1),(1,0)]
def calculate_path_old():
    temp_pos = [0,0,3,0,0,calculate_heuristic(0,0)]
    temp_pos2 = [0,0,2,0,0,calculate_heuristic(0,0)]
    open_positions: dict[tuple,list] = {
        tuple(temp_pos[:4]): temp_pos,
        tuple(temp_pos2[:4]): temp_pos2,
    }
    checked_positions = set()
    path_heat = -1
    while path_heat == -1:
        position_to_check_t = min(open_positions,key= lambda k: open_positions[k][-2] + open_positions[k][-1])
        position_to_check = open_positions[position_to_check_t]
        del open_positions[position_to_check_t]
        #print(checked_positions)
        for d in range(4):
            if abs(d-position_to_check[2]) == 2:
                continue
            if position_to_check[2] == d and position_to_check[3] == 3:
                continue
            new_x = position_to_check[1] + dir_sums[d][1]
            new_y = position_to_check[0] + dir_sums[d][0]
            if  new_x >= len(heat_loss_map[0]) or new_x < 0 or new_y >= len(heat_loss_map) or new_y < 0:
                continue
            # If it is the end
            if new_x == len(heat_loss_map[0])-1 and new_y == len(heat_loss_map)-1:
                path_heat = position_to_check[-2] + heat_loss_map[new_y][new_x]
                break

            st_pth_len = 1 if d != position_to_check[2] else position_to_check[3] + 1
            new_position = [new_y,new_x,d,st_pth_len,position_to_check[-2] + heat_loss_map[new_y][new_x],calculate_heuristic(new_y,new_x)]
            new_position_t = tuple(new_position[:4])
            if new_position_t in open_positions:
                if open_positions[new_position_t][-2] > new_position[-2]:
                    open_positions[new_position_t] = new_position
                continue
            if new_position_t not in checked_positions: 
                open_positions[new_position_t] = new_position

        checked_positions.add(position_to_check_t)
    return path_heat

def calculate_path():
    temp_pos = (0,0,3,0)
    temp_pos2 = (0,0,2,0)
    heat_per_pos: dict[tuple,int] = {
        tuple(temp_pos): 0,
        tuple(temp_pos2): 0,
    }
    open_positions = list(heat_per_pos.keys())
    while len(open_positions) > 0:
        new_positions = []
        for y,x,dir,nsteps in open_positions:
            for d in range(4):
                if abs(d-dir) == 2:
                    continue
                if nsteps == 3 and d == dir:
                    continue
                new_x = x + dir_sums[d][1]
                new_y = y + dir_sums[d][0]
                if  new_x >= len(heat_loss_map[0]) or new_x < 0 or new_y >= len(heat_loss_map) or new_y < 0:
                    continue
                new_nsteps = 1 if d != dir else nsteps + 1
                new_key = (new_y,new_x,d,new_nsteps)
                new_heat = heat_per_pos[(y,x,dir,nsteps)] + heat_loss_map[y][x]
                if new_key not in heat_per_pos or heat_per_pos[new_key] > new_heat:
                    heat_per_pos[new_key] = new_heat
                    new_positions.append(new_key)
        open_positions = new_positions
    print(len(heat_per_pos))
    return min(heat_per_pos[i] for i in heat_per_pos if i[0] == len(heat_loss_map)-1 and i[1] == len(heat_loss_map[0])-1)

print(calculate_path()+1)
