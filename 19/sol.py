import re

file = open("19/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

# Parse Rules
name_rgx = re.compile('(.*)(?:{)')
rule_rgx = re.compile('(?:{|,)(.*?)(<|>)(\d*)(?::)(.*?)(?=,)')
final_rgx = re.compile('(?<=,)(\w*?)(?:})')
next_part_indx = 0

rules: dict[str,list] = dict()
for i,l in enumerate(lines):
    if l == '': 
        next_part_indx = i
        break
    rule_name = re.findall(name_rgx,l)[0]
    rule_values = re.findall(rule_rgx,l)
    end_send = re.findall(final_rgx,l)[0]
    rule_values.append(end_send)
    rules[rule_name] = rule_values

# Parse the parts
part_values_rgx = re.compile('(\w)(?:=)(\d*)')

parts = []
for l in lines[next_part_indx+1:]:
    part_values = re.findall(part_values_rgx,l)
    part = {i:int(j) for i,j in part_values}
    parts.append(part)

# print(rules)
# print(parts)
    
accepted_parts = []
for p in parts:
    current_rule = 'in'
    while True:
        for var,symb,num,send in rules[current_rule][:-1]:
            if symb == '<':
                if p[var] < int(num): 
                    current_rule = send
                    break
            if symb == '>':
                if p[var] > int(num): 
                    current_rule = send
                    break
        else:
            current_rule = rules[current_rule][-1]
        if current_rule == 'A':
            accepted_parts.append(p)
            break
        elif current_rule == 'R':
            break

tot = 0
ratings = ['s','m','a','x']
for p in accepted_parts:
    for c in ratings:
        tot += p[c]
print(tot)
