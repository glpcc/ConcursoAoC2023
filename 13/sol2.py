import numpy as np

file = open("13/input.txt", "r")

lines = [i.strip() for i in file.readlines()]


all_squares: list[np.ndarray] = []
current_square = []
for l in lines:
    if l == '':
        all_squares.append(np.array(current_square))
        current_square = []
    else:
        current_line = [1 if i == '#' else 0 for i in l]
        current_square.append(current_line)
all_squares.append(np.array(current_square))
#print(all_squares)

def print_square(sq):
    for i in sq:
        for j in i:
            print('#' if j == 1 else '.',end='')
        print()

tot = 0
for square in all_squares:
    mirrored_vertical_square = square[:,::-1]
    # See if there is vertical mirroring
    bes_index = 'a'
    corrs = []
    for i in range(-len(square[0])+2,len(square[0])-1):
        if i ==0:
            continue
        elif i >= 1:
            corr = np.sum(np.abs(square[:,i:] - mirrored_vertical_square[:,:-i]))
        else:
            corr = np.sum(np.abs(square[:,:i] - mirrored_vertical_square[:,-i:]))

        if corr == 2 and (len(square[0]) - abs(i)) % 2 == 0:
            bes_index = i
            break
        
    if bes_index != 'a':
        mirror_size = (len(square[0]) - abs(bes_index)) // 2 + (bes_index if bes_index > 0 else 0)
        tot += mirror_size
        # print(f'Vertical mirror in index {mirror_size}',len(square[0]),bes_index)
        # if bes_index > 0:
        #     print_square(square[:,bes_index:])
        # else:
        #     print_square(square[:,:bes_index])
        # continue

    # See Horizontal mirroring
    mirrored_horizontal_square = square[::-1]
    bes_index = 'a'
    corrs = []
    for i in range(-len(square)+2,len(square)-1):
        if i ==0:
            continue
        elif i >= 1:
            corr = np.sum(np.abs(square[i:] - mirrored_horizontal_square[:-i]))
        else:
            corr = np.sum(np.abs(square[:i] - mirrored_horizontal_square[-i:]))
        if corr == 2 and (len(square[0]) - abs(i)) % 2 == 0:
            bes_index = i
            break


    if bes_index != 'a':
        mirror_size = (len(square) - abs(bes_index)) // 2 + (bes_index if bes_index > 0 else 0)
        tot += 100*mirror_size
        # print(f'Horizontal mirror in index {mirror_size}',len(square),bes_index)
        # if bes_index > 0:
        #     print_square(square[bes_index:])
        # else:
        #     print_square(square[:bes_index])


print(tot)