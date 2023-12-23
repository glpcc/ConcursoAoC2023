

file = open("23/input.txt", "r")

lines = [i.strip() for i in file.readlines()]
maze = lines

positions_path_lengths = {
    (0,1): -1
}
directions = [(-1,0),(1,0),(0,1),(0,-1)]

start = (0,1)
start2 = (1,1)
end = (len(maze)-1,len(maze[0])-2)
paths = [({start},start2)]

while len(paths) > 0:
    new_paths = []
    for path,head in paths:
        max_known_path = positions_path_lengths.get(head,-1)
        if len(path) > max_known_path:
            positions_path_lengths[head] = len(path)
        else:
            continue
        if head == end:
            continue
        y = head[0]
        x = head[1]
        for dy,dx in directions:
            if maze[y+dy][x+dx] != '#' and (y+dy,x+dx) not in path:
                new_paths.append((path | {(y+dy,x+dx)},(y+dy,x+dx)))
    paths = new_paths

# for y in range(len(maze)):
#     for x in range(len(maze[0])):
#         if (y,x) in positions_path_lengths:
#             print('O', end='')
#         else:
#             print(maze[y][x], end='')
#     print()

print(positions_path_lengths[end])