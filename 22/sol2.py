

file = open("22/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

bricks = []
for l in lines:
    start, finish = l.split('~')
    start = tuple([int(i) for i in start.split(',')])
    finish = tuple([int(i) for i in finish.split(',')])
    d = 0
    for i in range(3):
        if start[i] != finish[i]:
            d = i
            break
    bricks.append((start,finish,d))

bricks = sorted(bricks,key=lambda k: k[0][2])


def fall_bricks(bricks):
    new_bricks = []
    map_settlements = dict()
    supporting = {i:[] for i in range(len(bricks))}
    suported_by = [0 for i in bricks]
    bricks_fallen = 0
    for bindx,((sx,sy,sz),(fx,fy,fz),d) in enumerate(bricks):
        falling = True
        falled = False
        unique_supports = set()
        while falling:
            unique_supports = set()
            # Check if there is bricks below
            match d:
                case 0:
                    for i in range(fx-sx+1):
                        if (sx+i,sy,sz-1) in map_settlements:
                            falling = False
                            unique_supports.add(map_settlements[(sx+i,sy,sz-1)])
                case 1:
                    for i in range(fy-sy+1):
                        if (sx,sy+i,sz-1) in map_settlements:
                            falling = False
                            unique_supports.add(map_settlements[(sx,sy+i,sz-1)])
                case 2:
                    if (sx,sy,sz-1) in map_settlements:
                        falling = False
                        unique_supports.add(map_settlements[(sx,sy,sz-1)])
            if falling:
                if sz <= 1:
                    falling = False
                    break
                sz -= 1
                fz -= 1
                falled = True
        if falled:
            bricks_fallen += 1
        suported_by[bindx] = len(unique_supports)
        for indx in unique_supports:
            supporting[indx].append(bindx)
        # Register the positions of the brick
        new_bricks.append(((sx,sy,sz),(fx,fy,fz),d))
        match d:
                case 0:
                    for i in range(fx-sx+1):
                        map_settlements[(sx+i,sy,sz)] = bindx
                case 1:
                    for i in range(fy-sy+1):
                        map_settlements[(sx,sy+i,sz)] = bindx
                case 2:
                    for i in range(fz-sz+1):
                        map_settlements[(sx,sy,sz+i)] = bindx
    return new_bricks,supporting,suported_by,bricks_fallen


new_bricks,supporting,suported_by,bricks_fallen = fall_bricks(bricks)
# print(supporting)
# print(suported_by)
tot = 0
for indx in supporting:
    if not all(suported_by[i] > 1 for i in supporting[indx]):
        copy_bricks = new_bricks.copy()
        del copy_bricks[indx]
        _,_,_,bricks_fallen = fall_bricks(copy_bricks)
        tot += bricks_fallen
print(tot)
