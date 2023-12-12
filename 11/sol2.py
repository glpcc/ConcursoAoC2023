import numpy as np
import queue

def turn(prev_direction, character):
    match character:
        case '|':
            return (prev_direction[0],0)
        case '7':
            return (prev_direction[0]+1,prev_direction[1]-1)
        case '-':
            return (0,prev_direction[1])
        case 'L':
            return (prev_direction[0]-1, prev_direction[1]+1)
        case 'J':
            return (prev_direction[0]-1, prev_direction[1]-1)
        case 'F':
            return (prev_direction[0]+1, prev_direction[1]+1)
        case _ :
            print(f'Error hay un caracter no reconocido: {character}')
            return prev_direction


file = open("10/input.txt", "r")

lines = [[j for j in i.strip()] for i in file.readlines()]

matrix = np.array(lines)
s_pos = np.where(matrix == 'S')
s_pos = (s_pos[0][0],s_pos[1][0])
print(matrix[s_pos[0]][s_pos[1]])

loop_length = 1



# I Hardcode the position of the next node because it is way easier
next_pos = (s_pos[0]+1,s_pos[1])
current_direction = (1,0)
loop_positions_set = {next_pos,s_pos}
loop_positions_list = [next_pos]

while matrix[next_pos[0]][next_pos[1]] != 'S':
    current_char = matrix[next_pos[0]][next_pos[1]]
    current_direction = turn(current_direction,current_char)
    next_pos = (next_pos[0] + current_direction[0],next_pos[1] + current_direction[1])
    loop_positions_set.add(next_pos)
    loop_positions_list.append(next_pos)
    loop_length += 1

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if (y,x) not in loop_positions_set:
            matrix[y][x] = '.'

print(matrix)


alredy_looked_positions = set()
positions_to_look = queue.LifoQueue()

row_length = len(matrix[0])
colum_length  = len(matrix)

def look_position(y,x):
    temp = (y % colum_length,x % row_length)
    if matrix[temp[0]][temp[1]] == '.' and temp not in alredy_looked_positions:
        # print(f'Looked at position: {temp}')
        positions_to_look.put(temp)
        alredy_looked_positions.add(temp)
# Loop over the cycle positions around the outside to populate the positions to look queue
current_side = 0 # 0 -> left, 1 -> down , 2 -> right , 3 -> up
for y,x in loop_positions_list:
    character = matrix[y][x]
    match character:
        case '|':
            look_position(y,x + (current_side-1))
        case '-':
            look_position(y + (1 if current_side == 1 else -1),x)
        case '7':
            if current_side == 3 or current_side == 2:
                look_position(y-1,x)
                look_position(y,x+1)
                current_side = 2 if current_side == 3 else 3
            else:
                current_side = 1 if current_side == 0 else 0
        case 'L':
            if current_side == 3 or current_side == 2:
                current_side = 2 if current_side == 3 else 3
            else:
                look_position(y+1,x)
                look_position(y,x-1)
                current_side = 1 if current_side == 0 else 0
        case 'F':
            if current_side == 0 or current_side == 3:
                look_position(y-1,x)
                look_position(y,x-1)
                current_side = 3 if current_side == 0 else 0
            else:
                current_side = 1 if current_side == 2 else 2
        case 'J':
            if current_side == 0 or current_side == 3:
                current_side = 3 if current_side == 0 else 0
            else:
                look_position(y+1,x)
                look_position(y,x+1)
                current_side = 1 if current_side == 2 else 2

# search over the queue of points to count points outside
while not positions_to_look.empty():
    y,x = positions_to_look.get()
    look_position(y+1,x)
    look_position(y,x+1)
    look_position(y-1,x)
    look_position(y,x-1)


# visualization to debug 
# matrix2 = matrix.copy()
# for j in range(len(matrix)):
#     for i in  range(len(matrix[j])):
#         if (j,i) in alredy_looked_positions:
#             print('$',end='')
#         else:
#             print(matrix2[j][i],end='')
#     print()
print((row_length*colum_length) - (len(alredy_looked_positions) + len(loop_positions_list)))
print(len(alredy_looked_positions)) # Complementary to the one before

# print(loop_positions_list)