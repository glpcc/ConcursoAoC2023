

file = open("22/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

bricks = []
for l in lines:
    start, finish = l.split('~')
    start = tuple([int(i) for i in start.split(',')])
    finish = tuple([int(i) for i in finish.split(',')])
    d = 0
    for i in range(3):
        if start[i] != finish[i]:
            d = i
            break
    bricks.append((start,finish,d))

bricks = sorted(bricks,key=lambda k: k[0][2])
map_settlements = dict()
supporting = {i:[] for i in range(len(bricks))}
suported_by = [0 for i in bricks]
for bindx,((sx,sy,sz),(fx,fy,fz),d) in enumerate(bricks):
    falling = True
    unique_supports = set()
    while falling:
        unique_supports = set()
        # Check if there is bricks below
        match d:
            case 0:
                for i in range(fx-sx+1):
                    if (sx+i,sy,sz-1) in map_settlements:
                        falling = False
                        unique_supports.add(map_settlements[(sx+i,sy,sz-1)])
            case 1:
                for i in range(fy-sy+1):
                    if (sx,sy+i,sz-1) in map_settlements:
                        falling = False
                        unique_supports.add(map_settlements[(sx,sy+i,sz-1)])
            case 2:
                if (sx,sy,sz-1) in map_settlements:
                    falling = False
                    unique_supports.add(map_settlements[(sx,sy,sz-1)])
        if falling:
            if sz <= 1:
                falling = False
                break
            sz -= 1
            fz -= 1
    suported_by[bindx] = len(unique_supports)
    for indx in unique_supports:
        supporting[indx].append(bindx)
    # Register the positions of the brick
    match d:
            case 0:
                for i in range(fx-sx+1):
                    map_settlements[(sx+i,sy,sz)] = bindx
            case 1:
                for i in range(fy-sy+1):
                    map_settlements[(sx,sy+i,sz)] = bindx
            case 2:
                for i in range(fz-sz+1):
                    map_settlements[(sx,sy,sz+i)] = bindx

# print(supporting)
# print(suported_by)
tot = 0
for indx in supporting:
    if all(suported_by[i] > 1 for i in supporting[indx]):
        tot +=1 
print(tot)
# print(map_settlements)
# def print_test():
#     for i in range(10):
#         for j in range(3):
#             if (j,0,i) in map_settlements:
#                 print(map_settlements[(j,0,i)],end='')
#             else:
#                 print('.',end='')
#         print()
# print_test()

# # Visualize the map_settlements as cubes in 3d
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.set_xlim(0,10)
# ax.set_ylim(0,10)
# ax.set_zlim(0,10)
# colors = ['r','g','b','y','c','m','k','w']
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             if (i,j,k) in map_settlements:
#                 ax.scatter(i,j,k,c=colors[map_settlements[(i,j,k)]%len(colors)],marker='s')

# plt.show()