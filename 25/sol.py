import networkx as nx
from matplotlib import pyplot as plt

file = open("25/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

created_nodes = set()
G = nx.Graph()

for l in lines:
    node, connections = l.split(":")
    connections = connections.strip().split(" ")
    if node not in created_nodes:
        G.add_node(node)
        created_nodes.add(node)
    for c in connections:
        if c not in created_nodes:
            G.add_node(c)
            created_nodes.add(c)
        G.add_edge(node, c)

# plot graph
pos=nx.spring_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

# By visualization, the edges to erase are, qnz-gzr, hgk-pgz, xgs-lmj
# Erase those edges
G.remove_edge("qnz", "gzr")
G.remove_edge("hgk", "pgz")
G.remove_edge("xgs", "lmj")

# count the size of the two subgraphs
print(len(nx.node_connected_component(G, "npn"))* len(nx.node_connected_component(G, "fgz")))

