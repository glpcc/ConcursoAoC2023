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

ratings = ['s','m','a','x']
parts = [{i:(1,4000) for i in ratings}]


# print(rules)
# print(parts)
def calculate_num_accepted(rule,p):
    if rule == 'R': return 0
    if rule == 'A':
        tot = 1
        for r in ratings:
            tot *= p[r][1]-p[r][0] + 1
        return tot
    num_accepted = 0
    for var,symb,num,send in rules[rule][:-1]:
        num = int(num)
        if symb == '<':
            if p[var][0] < num and p[var][1] >= num:
                new_p = p.copy()
                new_p[var] = (p[var][0],num-1)
                num_accepted += calculate_num_accepted(send,new_p)
                p[var] = (num,p[var][1])
            elif p[var][1] < num:
                return calculate_num_accepted(send,p) + num_accepted
        if symb == '>':
            if p[var][0] > num:
                return calculate_num_accepted(send,p) + num_accepted
            elif p[var][0] <= num and p[var][1] > num:
                new_p = p.copy()
                new_p[var] = (num+1,p[var][1])
                num_accepted += calculate_num_accepted(send,new_p)
                p[var] = (p[var][0],num)
    else:
        current_rule = rules[rule][-1]
    # print(num_accepted)
    if current_rule == 'A':
        tot = 1
        for r in ratings:
            tot *= p[r][1]-p[r][0] + 1
        return num_accepted + tot
    elif current_rule == 'R':
        return num_accepted
    else:
        return calculate_num_accepted(current_rule,p) + num_accepted

accepted_parts = []
tot = 0
current_rule = 'in'
tot += calculate_num_accepted(current_rule,parts[0])
print(tot)

