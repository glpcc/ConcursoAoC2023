import numpy as np

file = open("12/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

springs = []
numbers = []

# for l in lines:
#     s,n = l.split(' ')
#     n = [int(i) for i in n.split(',')] * 5
#     s = [i for i in s] + ['?']
#     s = s *5
#     s = s[:-1]
#     springs.append(s)
#     numbers.append(n)

for l in lines:
    s,n = l.split(' ')
    n = [int(i) for i in n.split(',')]
    s = [i for i in s]
    springs.append(s)
    numbers.append(n)

# print(''.join(springs[0]))
# print(numbers)

def count_posibilities(str_springs, number_list):
    # print(''.join(str_springs),number_list)
    if len(str_springs) == 0 and len(number_list) == 0: 
        # print(''.join(str_springs),number_list,'hey')
        return 1
    if len(number_list) == 0:
        # print(''.join(str_springs),number_list,'hey' if '#' not in str_springs else '')
        return 1 if '#' not in str_springs else 0
    inside_patch = False
    current_patch_size = 0
    n_index = -1
    spr_copy = str_springs.copy()
    for i, s in enumerate(str_springs):
        if s == '#':
            if inside_patch:
                current_patch_size += 1
                if current_patch_size > number_list[n_index]: return 0
            else:
                inside_patch = True
                current_patch_size = 1
                n_index += 1
                if n_index >= len(number_list): return 0
        elif s == '?':
            if inside_patch:
                diff = number_list[n_index] - current_patch_size
                # print(i+diff,''.join(spr_copy),diff,i)
                if i + diff - 1 >= len(str_springs): return 0
                for j in range(diff):
                    # Cant make the patch long enough
                    if spr_copy[i+j] == '.': return 0
                    spr_copy[i+j] = '#'

                if i + diff  < len(str_springs): 
                    # print(i+diff,''.join(str_springs),diff,i)
                    if str_springs[i+diff] == '#': return 0
                    spr_copy[i+diff] = '.'
                    # print(i+diff,''.join(spr_copy),diff,i)
                    return count_posibilities(spr_copy[i+diff:],number_list[n_index+1:])
                else:
                    return count_posibilities(spr_copy[i+diff:],number_list[n_index+1:])
            else:
                temp = 0
                spr_copy[i] = '.'
                a = count_posibilities(spr_copy[i:],number_list[n_index+1:])
                temp += a
                # if a > 0: print(''.join(spr_copy),number_list,'hey', a)
                spr_copy[i] = '#'
                a = count_posibilities(spr_copy[i:],number_list[n_index+1:])
                temp += a
                # if a > 0: print(''.join(spr_copy),number_list,'hey', a)
                return temp
        else:
            if inside_patch:
                if current_patch_size < number_list[n_index]: return 0
                inside_patch = False
    # if n_index == len(number_list) -1:
    #     print(''.join(str_springs),number_list,'hey')
    return 1 if n_index == len(number_list)-1 and current_patch_size == number_list[n_index] else 0

sol = 0
for s,n in zip(springs,numbers):
    a = count_posibilities(s,n)
    # print(''.join(s),a)
    sol += a 
print(sol)