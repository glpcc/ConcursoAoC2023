file = open("3/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

x_coord = 0
y_coord = 0
symbol_coords: set[tuple[int,int]] = set()
num_coords: set[tuple[int,int,int]] = set()
for y_coord,line in enumerate(lines):
    parsing_num = False
    num_pos = 0
    for x_coord,c in enumerate(line):
        if c.isdigit():
            if not parsing_num:
                parsing_num = True
                num_pos = x_coord
        elif c != '.':
            symbol_coords.add((x_coord,y_coord))
            # print(c,(x_coord,y_coord))
        if parsing_num and not c.isdigit():
            num = line[num_pos:x_coord]
            num_i = int(num)
            num_coords.add((num_i,num_pos,y_coord))
            parsing_num = False

    if parsing_num:
        num = int(line[num_pos:])
        num_coords.add((num,num_pos,y_coord))
        parsing_num = False

# print(num_coords)
# print(symbol_coords)


tot = 0
for num,coord_x,coord_y in num_coords:
    part_number = False
    number_len = len(str(num))
    # Check the top and bottom positions along the number
    for x_pad in range(-1,number_len+1):
        if (coord_x + x_pad,coord_y+1) in symbol_coords:
            # print(f'Num: {num} with symbol in {(coord_x + x_pad,coord_y+1)}')
            part_number = True
            break
        if (coord_x + x_pad,coord_y-1) in symbol_coords:
            # print(f'Num: {num} with symbol in {(coord_x + x_pad,coord_y-1)}')
            part_number = True
            break
    # Check the sides
    if (coord_x -1,coord_y) in symbol_coords:
        part_number = True
    if (coord_x +number_len,coord_y) in symbol_coords:
        part_number = True

    if part_number:
        print(num)
        tot += num

print(tot)
