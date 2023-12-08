

file = open("7/input.txt", "r")

lines = [i.strip() for i in file.readlines()]


hand_type_value = {
    'Five of a kind': 1e17,
    'Poker': 1e16,
    'Full': 1e15,
    'triple':1e14,
    'two pair':1e13,
    'pair': 1e12,
    'high': 0
}
card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
def get_hand_type_value(cards: str):
    card_nums = dict()
    for c in cards:
        if c not in card_nums:
            card_nums[c] = 1
        else:
            card_nums[c] += 1
    num_jokers = 0
    if 'J' in card_nums:
        num_jokers = card_nums['J']
        del card_nums['J']
    card_nums_list = sorted([[i,card_nums[i]] for i in card_nums],key= lambda k: k[1],reverse=True)
    if len(card_nums_list) == 0:
        card_nums_list.append(['J',0])
    card_nums_list[0][1] += num_jokers
    if card_nums_list[0][1] == 5:
        return hand_type_value['Five of a kind']
    elif card_nums_list[0][1] == 4:
        return hand_type_value['Poker']
    elif card_nums_list[0][1] == 3:
        if card_nums_list[1][1] == 2:
            return hand_type_value['Full']
        else:
            return hand_type_value['triple']
    elif card_nums_list[0][1] == 2:
        if card_nums_list[1][1] == 2:
            return hand_type_value['two pair']
        else:
            return hand_type_value['pair']
    else:
        return hand_type_value['high']

def get_cards_values(cards: str):
    return sum((100**(len(cards)-i))*card_values[c] for i,c in enumerate(cards))



hands = [i.split(' ') for i in lines ]
hand_ranking = sorted([(get_hand_type_value(h[0])+get_cards_values(h[0]),h[1]) for h in hands],key= lambda k: k[0], reverse=True)
#print(hand_ranking)
tot_sum = sum( (len(hand_ranking) - i)*int(hand_ranking[i][1]) for i in range(len(hand_ranking)))
print(tot_sum)

print(get_cards_values('KKK6A'))
print(get_cards_values('KKK72'))