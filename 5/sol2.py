import re

file = open("5/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

regxd = re.compile('\d+')
seeds = [int(i) for i in re.findall(regxd,lines[0])]
seeds_ranges = [(seeds[i],seeds[i+1]) for i in range(0,len(seeds)-1,2)]
print(seeds_ranges)
i = 3
maps: list[list[int,int,int]] = []
while i <= len(lines):
    # Lazy logic so no error out of range
    if i == len(lines) or lines[i] == '':
        # Finished a map
        # Iterate to find the new thing number
        new_things_ranges = []
        # print(maps)
        for start,rng_s in seeds_ranges:
            remaining_ranges = [(start,rng_s)]
            for new,old,rng in maps:
                new_remaining_ranges = []
                # print(f'Mapping ({old},{rng}) to seed {start},{rng_s}')
                for strt2, rng_s2 in remaining_ranges:
                    if strt2 + rng_s2 <= old or strt2 > old + rng:
                        new_remaining_ranges.append([strt2,rng_s2])
                        continue
                    left_cut = [strt2,old-strt2]
                    middle_left_cut = [old,rng_s2 - (old-strt2)]
                    middle_right_cut = [strt2, rng - (strt2 - old)]
                    right_cut = [old+rng,rng_s2 - (old+rng - strt2)]
                    if strt2 < old:
                        if strt2 + rng_s2 <= old + rng:
                            new_remaining_ranges.append(left_cut)
                            new_things_ranges.append([new,middle_left_cut[1]])
                        elif strt2 + rng_s2 > old + rng:
                            new_remaining_ranges.append(left_cut)
                            new_remaining_ranges.append(right_cut)
                            new_things_ranges.append([new,rng])
                    elif strt2 >= old:
                        if strt2 + rng_s2 <= old + rng:
                            new_things_ranges.append([new + (strt2-old),rng_s2])
                        else:
                            new_things_ranges.append([new + (strt2-old),rng - (strt2- old)])
                            new_remaining_ranges.append(right_cut)
                # print(new_remaining_ranges)
                # print(new_things_ranges)
                remaining_ranges = new_remaining_ranges
                if len(new_remaining_ranges) == 0:
                    break
                # print(remaining_ranges)
            if len(remaining_ranges) > 0:
                new_things_ranges += remaining_ranges
        seeds_ranges = new_things_ranges
        # print(seeds_ranges)
        maps = []
        i += 2
    elif lines[i] != '':
        maps.append([int(i) for i in re.findall(regxd,lines[i])])
        i += 1

print(min(seeds_ranges,key= lambda k: k[0]))

