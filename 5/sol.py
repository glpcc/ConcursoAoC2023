import re

file = open("5/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

regxd = re.compile('\d+')
seeds = [int(i) for i in re.findall(regxd,lines[0])]
print(seeds)
i = 3
maps: list[list[int,int,int]] = []
while i <= len(lines):
    # Lazy logic so no error out of range
    if i == len(lines) or lines[i] == '':
        # Finished a map
        # Iterate to find the new thing number
        new_things = []
        for s in seeds:
            found_match = False
            for new,old,rng in maps:
                if 0 <= s - old <= rng:
                    new_things.append(new + (s-old))
                    found_match = True
                    break
            if not found_match:
                new_things.append(s)
        seeds = new_things
        # print(seeds)
        maps = []
        i += 2
    elif lines[i] != '':
        maps.append([int(i) for i in re.findall(regxd,lines[i])])
        i += 1

print(min(seeds))

