import numpy as np

file = open("16/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

mirror_map = [[i for i in l] for l in lines]

rays = [(0,-1,'r')]

computed_rays = {rays[0]}
visited_positions = {(rays[0][0],rays[0][1])}

directions = {
    'r':(0,1),
    'l':(0,-1),
    'u':(-1,0),
    'd':(1,0)
}
directions_changes = {
    '\\': {
        'u': 'l',
        'd': 'r',
        'l': 'u',
        'r': 'd'
    },
    '/': {
        'u': 'r',
        'd': 'l',
        'l': 'd',
        'r': 'u'
    }
}

while len(rays) > 0:
    new_rays = []
    for y,x,d in rays:
        new_x = directions[d][1] + x
        new_y = directions[d][0] + y
        if new_x >= len(mirror_map[0]) or new_y >= len(mirror_map) or new_x < 0 or new_y < 0:
            continue
        match mirror_map[new_y][new_x]:
            case '.':
                new_rays.append((new_y,new_x,d))
            case '\\':
                new_dir = directions_changes['\\'][d]
                new_rays.append((new_y,new_x,new_dir))
            case '/':
                new_dir = directions_changes['/'][d]
                new_rays.append((new_y,new_x,new_dir))
            case '-':
                if d == 'u' or d == 'd':
                    new_rays.append((new_y,new_x,'l'))
                    new_rays.append((new_y,new_x,'r'))
                else:
                    new_rays.append((new_y,new_x,d))
            case '|':
                if d == 'l' or d == 'r':
                    new_rays.append((new_y,new_x,'u'))
                    new_rays.append((new_y,new_x,'d'))
                else:
                    new_rays.append((new_y,new_x,d))
    new_rays = [i for i in new_rays if i not in computed_rays]
    computed_rays = computed_rays.union(set(new_rays))
    rays = new_rays

visited_positions = set((i[0],i[1]) for i in computed_rays)
print(len(visited_positions) -1)

                        
