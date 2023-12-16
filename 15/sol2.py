import numpy as np

file = open("15/input.txt", "r")

line = file.readline().strip()

strs = list(line.split(','))

def get_hash(s: str):
    hsh = 0
    for chr in s:
        hsh += ord(chr)
        hsh *= 17
        hsh = hsh%256
    return hsh

def print_boxes(boxes):
    for i,box in enumerate(boxes):
        if len(box) > 0:
            print(f'Box: {i}, Inside: {box}')


tot = 0
boxes = [[] for i in range(256)]

for s in strs:
    
    symbl_indx = 0
    for i,c in enumerate(s):
        if c == '-' or c == '=':
            symbl_indx = i
            break
    label = s[:symbl_indx]
    h = get_hash(label)
    symbol = s[symbl_indx]
    if symbol == '=':
        focal_length = int(s[symbl_indx+1:])
        for i,(lbl,fl) in enumerate(boxes[h]):
            if lbl == label:
                boxes[h][i] = (label,focal_length)
                break
        else:
            boxes[h].append((label,focal_length))
    elif symbol == '-':
        positions_to_delete = []
        for i,(lbl,fl) in enumerate(boxes[h]):
            if lbl == label:
                positions_to_delete.append(i)
        for i in positions_to_delete:
            del boxes[h][i]
    # print_boxes(boxes)
    # print()
# print_boxes(boxes)
# Calculate focusing power
for i,box in enumerate(boxes):
    for j,lens in enumerate(box):
        tot += (i+1) * (j+1) * lens[1]

print(tot)