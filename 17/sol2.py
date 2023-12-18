

file = open("17/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

heat_loss_map = [[int(i) for i in l] for l in lines]



def paint_map(positions):
    for y in range(len(heat_loss_map)):
        for x in range(len(heat_loss_map[y])):
            print('#' if (y,x) in positions else '.',end='')
        print()
    print()

# Las direcciones son 0 izq, 1 up , 2 right, 3 down
dir_sums = [(0,-1),(-1,0),(0,1),(1,0)]
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
                if nsteps == 10 and d == dir:
                    continue
                if nsteps < 4 and d != dir:
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
    return min(heat_per_pos[i] for i in heat_per_pos if i[0] == len(heat_loss_map)-1 and i[1] == len(heat_loss_map[0])-1 and i[3] >= 4)

print(calculate_path()+1)
