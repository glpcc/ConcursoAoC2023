import numpy as np


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
next_pos = [s_pos[0]-1,s_pos[1]]
current_direction = (-1,0)

while matrix[next_pos[0]][next_pos[1]] != 'S':
    current_char = matrix[next_pos[0]][next_pos[1]]
    current_direction = turn(current_direction,current_char)
    next_pos[0] += current_direction[0]
    next_pos[1] += current_direction[1]
    loop_length += 1

print(loop_length/2)