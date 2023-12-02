file = open("2/input.txt", "r")

lines = [i.strip() for i in file.readlines()]


max_values = {
    'red': 12,
    'blue':14,
    'green':13
}
sum_ids = 0

for line in lines:
    game, rest = line.split(':')
    sets = list(rest.split(';'))
    game_id = int(game[4:])
    valid = True
    for s in sets:
        if not valid: break
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
            if pulled_values[color] > max_values[color]:
                valid = False
                break
    if valid:
        sum_ids += game_id
print(sum_ids)

