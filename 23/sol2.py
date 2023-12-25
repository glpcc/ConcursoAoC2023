import networkx
import queue
import time
from matplotlib import pyplot as plt
file = open("23/input.txt", "r")

lines = [i.strip() for i in file.readlines()]
maze = lines

crossroad_graph = networkx.Graph()

positions_path_lengths = {
    (0,1): -1
}

directions = [(-1,0),(1,0),(0,1),(0,-1)]

start = (0,1)
current_node = start
crossroad_graph.add_node(current_node)
start2 = (1,1)
end = (len(maze)-1,len(maze[0])-2)
paths = [({start},start2)]
uncomputed_crossroads = queue.Queue()
uncomputed_crossroads.put(current_node)
crossroads_posible_dirs = {
    (0,1): [(1,1)]
}
while not uncomputed_crossroads.empty():
    current_node = uncomputed_crossroads.get()
    if current_node == end:
        break
    paths = [({current_node},i) for i in crossroads_posible_dirs[current_node]]
    while len(paths) > 0:
        new_paths = []
        for path,head in paths:
            y = head[0]
            x = head[1]
            posible_dirs = []
            if (y,x) == end:
                crossroad_graph.add_node((y,x))
                crossroad_graph.add_edge(current_node,(y,x),weight=len(path))
                uncomputed_crossroads.put((y,x))
                continue
            for dy,dx in directions:
                if maze[y+dy][x+dx] != '#' and ((y+dy,x+dx) not in path) :
                    posible_dirs.append((y+dy,x+dx))
            if len(posible_dirs) == 0: continue
            if len(posible_dirs) > 1 :
                crossroad_graph.add_node((y,x))
                crossroad_graph.add_edge(current_node,(y,x),weight=len(path))
                if (y,x) not in crossroads_posible_dirs:
                    uncomputed_crossroads.put((y,x))
                    crossroads_posible_dirs[(y,x)] = posible_dirs
            else:
                new_paths.append((path | {(y,x)},posible_dirs[0]))
        paths = new_paths

# Find the longest path by bruteforcing all paths
current_node = start
paths = [({start},i,crossroad_graph.get_edge_data(current_node,i)['weight']) for i in crossroad_graph[current_node]]
max_path_length = -1
max_lengts = {
    (0,1) : -1
}
# while paths:
#     new_paths = []
#     print(len(paths))
#     for path,head,length in paths:
#         for neib in crossroad_graph[head]:
#             if neib in path: continue
#             new_lenght = length + crossroad_graph.get_edge_data(head,neib)['weight']
#             if neib in max_lengts and new_lenght < max_lengts[neib] : continue
#             if neib == end:
#                 max_path_length = max(max_path_length,new_lenght)
#             else:
#                 new_paths.append((path | {head},neib,new_lenght))
#                 max_lengts[neib] = new_lenght
#     paths = new_paths
# print(max_path_length)



pos=networkx.spring_layout(crossroad_graph)
networkx.draw_networkx(crossroad_graph,pos)
labels = networkx.get_edge_attributes(crossroad_graph,'weight')
networkx.draw_networkx_edge_labels(crossroad_graph,pos,edge_labels=labels)
plt.show()
max_l = 0
for p in networkx.all_simple_edge_paths(crossroad_graph,start,end):
    max_l = max(max_l,sum(crossroad_graph.get_edge_data(i[0],i[1])['weight'] for i in p))
print(max_l)