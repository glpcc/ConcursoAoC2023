file = open("4/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

tot = 0
for line in lines:
    _, nums = line.split(':')
    win_nums, my_nums = nums.split('|')
    win_nums = set([int(i) for i in win_nums.strip().split(' ') if i != ''])
    my_nums = set([int(i) for i in my_nums.strip().split(' ') if i != ''])
    intersecction = set.intersection(win_nums,my_nums)
    if len(intersecction) > 0:
        tot += 2**(len(intersecction)-1)
print(tot)