import re

import get_input_data

dev_input = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]

real_input = get_input_data.get_input('day_4')


# row = dev_input[0]


def get_winning_numbers(row):
    iterable = re.finditer('[0-9]+ ', row[:row.index('|')])
    winning_numbers = list()
    for match in iterable:
        # print(int(match.group()))
        winning_numbers.append(int(match.group()))
    return winning_numbers


def get_ticket_numbers(row):
    iterable = re.finditer(' [0-9]+', row[row.index('|'):])
    winning_numbers = list()
    for match in iterable:
        # print(int(match.group()))
        winning_numbers.append(int(match.group()))
    return winning_numbers


def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def get_score(winning, ticket):
    if len(intersection(winning, ticket)) > 0:
        return 2 ** (len(intersection(winning, ticket)) - 1)
    else:
        return 0


def get_total_sum(the_input):
    total_sum = 0
    for row in the_input:
        winning = get_winning_numbers(row)
        ticket = get_ticket_numbers(row)
        total_sum += get_score(winning, ticket)
    return total_sum


print('-- PART 1 --')
print(get_total_sum(dev_input))
print(get_total_sum(real_input))

print('-- PART 2 --')


def get_card_nr(row):
    return int(re.findall('([\d]+):', row)[0])


def get_cards_dict(the_input):
    cards = dict()

    for row in the_input:
        cards[get_card_nr(row)] = row

    return cards


def get_children_of_row(row, card_number):
    winning = get_winning_numbers(row)
    ticket = get_ticket_numbers(row)

    length = len(intersection(winning, ticket))
    return list(range(card_number + 1, card_number + 1 + length))


def get_nr_of_children(input_dict, card_number, row):
    nr_of_children = 1

    for cn in get_children_of_row(row, card_number):
        # print(cn)
        # nr_of_children += 1
        nr_of_children += get_nr_of_children(input_dict, cn, input_dict[cn])

    return nr_of_children


def get_total_number_of_tickets(the_input):
    input_dict = get_cards_dict(the_input)

    total_sum = 0
    for k, v in input_dict.items():
        total_sum += get_nr_of_children(input_dict, k, v)

    return total_sum


print(get_total_number_of_tickets(dev_input))
print(get_total_number_of_tickets(real_input))
