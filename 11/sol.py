import numpy as np
import math


file = open("11/input.txt", "r")

lines = [[j for j in i.strip()] for i in file.readlines()]

galaxies = []

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            galaxies.append([y,x])

galaxies_sortedY = sorted(galaxies, key = lambda k: k[0])
past_y = -1
row_to_expand = 0
for i,(y,x)  in enumerate(galaxies_sortedY):
    row_to_expand += y - (past_y+1) if y != past_y else 0
    galaxies_sortedY[i][0] += row_to_expand*1000000 - row_to_expand
    past_y = y

# print(galaxies_sortedY)
past_x = -1
columns_to_expand = 0
galaxies_sortedX = sorted(galaxies_sortedY, key = lambda k: k[1])
for i,(y,x)  in enumerate(galaxies_sortedX):
    columns_to_expand += x - (past_x+1) if x != past_x else 0
    galaxies_sortedX[i][1] += columns_to_expand*1000000 - columns_to_expand
    past_x = x


len_matrix = [[-1 for i in range(len(galaxies_sortedX))] for j in range(len(galaxies_sortedX))]
for i in range(len(len_matrix)):
    for j in range(len(len_matrix[i])):
        if i >= j:
            len_matrix[i][j] = 0
            continue
        len_matrix[i][j] = abs(galaxies_sortedX[i][0] - galaxies_sortedX[j][0]) + abs(galaxies_sortedX[i][1] - galaxies_sortedX[j][1])

tot = 0
for i,row in enumerate(len_matrix):
    tot += sum(row)

print(tot)