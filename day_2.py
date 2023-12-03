import re

import get_input_data

dev_input = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

dev_limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

input1 = get_input_data.get_input('day_2')

row = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'


def get_game_nr(row):
    return int(re.findall('^Game ([\d]+):', row)[0])


def get_max_dice_for_color(row, color):
    return max(([int(i) for i in re.findall(' ([\d]+) ' + color, row)] + [0]))


def is_illegal(row, color, limit):
    return get_max_dice_for_color(row, color) > limit


def get_game_nr_or_zero(row, limits):
    if is_illegal(row, 'red', limits['red']) or is_illegal(row, 'green', limits['green']) or is_illegal(row, 'blue',
                                                                                                        limits['blue']):
        return 0
    else:
        return get_game_nr(row)


def get_game_power(row):
    return get_max_dice_for_color(row, 'red') * get_max_dice_for_color(row, 'green') * get_max_dice_for_color(row,
                                                                                                              'blue')


def get_sum_of_game_nr(rows, limits):
    return sum([get_game_nr_or_zero(row, limits) for row in rows])


def get_sum_of_game_power(rows):
    return sum([get_game_power(row) for row in rows])


print('-- PART 1 --')
print(get_sum_of_game_nr(dev_input, dev_limits))
print(get_sum_of_game_nr(input1, dev_limits))

print('-- PART 2 --')
print(get_sum_of_game_power(dev_input))
print(get_sum_of_game_power(input1))
