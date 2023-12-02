file = open("2/input.txt", "r")

lines = [i.strip() for i in file.readlines()]



sum_powers = 0

for line in lines:
    game, rest = line.split(':')
    sets = list(rest.split(';'))
    min_values = {
        'red': 0,
        'blue':0,
        'green':0
    }
    for s in sets:
        pulled_values = {
            'red': 0,
            'blue':0,
            'green':0
        }
        pulls = [i.strip() for i in s.split(',')]
        for p in pulls:
            num, color = p.split(' ')
            num = int(num)
            pulled_values[color] += num

        for color in pulled_values:
            min_values[color] = max(min_values[color],pulled_values[color])
    sum_powers += min_values['blue']*min_values['green']*min_values['red']

print(sum_powers)

