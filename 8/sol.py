file = open("8/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

instructions = lines[0].strip()

posible_nodes = {
    line[0:3] : (line[7:10],line[12:15]) for line in lines[2:]
}
current_node = 'AAA'
num_steps = 0
# print(instructions)
# print(posible_nodes)
while current_node != 'ZZZ':
    current_node = posible_nodes[current_node][1] if instructions[num_steps%len(instructions)] == 'R' else posible_nodes[current_node][0]
    num_steps += 1

print(num_steps)
