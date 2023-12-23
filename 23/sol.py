

file = open("23/input.txt", "r")

lines = [i.strip() for i in file.readlines()]
maze = lines

positions_path_lengths = {
    (0,1): -1
}
directions = [(-1,0),(1,0),(0,1),(0,-1)]
arrows = {
    '>': (0,1),
    '<': (0,-1),
    '^': (-1,0),
    'v': (1,0)
}

paths = [({(0,1)},(0,1))]
while len(paths) > 0:
    new_paths = []
    for path,head in paths:
        max_known_path = positions_path_lengths.get(head,-1)
        if len(path) > max_known_path:
            positions_path_lengths[head] = len(path)
            if head == (len(maze)-1,len(maze[0])-2):
                continue
        else:
            continue
        y = head[0]
        x = head[1]
        if maze[y][x] == '.':
            for dy,dx in directions:
                if maze[y+dy][x+dx] != '#' and (y+dy,x+dx) not in path:
                    new_paths.append((path | {(y+dy,x+dx)},(y+dy,x+dx)))
        else:
            dy, dx = arrows[maze[y][x]]
            if maze[y+dy][x+dx] != '#' and (y+dy,x+dx) not in path:
                    new_paths.append((path | {(y+dy,x+dx)},(y+dy,x+dx)))
    paths = new_paths

print(positions_path_lengths[(len(maze)-1,len(maze[0])-2)] -1 )