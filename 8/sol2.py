import math

file = open("8/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

instructions = lines[0].strip()

posible_nodes = {
    line[0:3] : (line[7:10],line[12:15]) for line in lines[2:]
}
current_nodes = [i for i in posible_nodes if i[2] == 'A']
num_steps = 0
# print(instructions)
# print(posible_nodes)
def next_node(node,i):
    return posible_nodes[node][1] if instructions[i%len(instructions)] == 'R' else posible_nodes[node][0]

steps_to_z = []
print(current_nodes)
while len(current_nodes) > 0:
    new_current_nodes = []
    
    for j in current_nodes:
        next_n = next_node(j,num_steps)
        # print(next_n,(num_steps+1) % len(instructions))
        if next_n[2] == 'Z' and (num_steps+1) % len(instructions) == 0:
            steps_to_z.append(num_steps+1)
        else:
            new_current_nodes.append(next_n)
    current_nodes = new_current_nodes

    num_steps += 1
print(steps_to_z)
print(math.lcm(*steps_to_z))
