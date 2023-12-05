file = open("4/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

tot = len(lines)
num_scratch_pads = {i:1 for i in range(len(lines))}

for i,line in enumerate(lines):
    _, nums = line.split(':')
    win_nums, my_nums = nums.split('|')
    win_nums = set([int(i) for i in win_nums.strip().split(' ') if i != '']) # Clean double spaces and split into ints
    my_nums = set([int(i) for i in my_nums.strip().split(' ') if i != ''])
    intersecction = set.intersection(win_nums,my_nums)
    if len(intersecction) > 0:
        tot += len(intersecction)*num_scratch_pads[i]
        for j in range(i+1,i+len(intersecction)+1):
            num_scratch_pads[j] += num_scratch_pads[i]
print(tot)