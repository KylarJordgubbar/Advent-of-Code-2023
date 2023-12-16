import get_input_data
import numpy as np

dev_input = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....'
]


def transpose(plate):
    plate = [list(i) for i in plate]
    plate = np.array(plate).T
    return plate


def tilt(plate):
    output = []
    for row in plate:
        place_for_rock = None
        cursor = 0
        while cursor < len(row):
            # print(row[cursor])

            if row[cursor] == '.' and place_for_rock is None:
                place_for_rock = cursor

            if row[cursor] == 'O' and place_for_rock is not None:
                row[place_for_rock] = 'O'
                row[cursor] = '.'
                cursor = place_for_rock
                place_for_rock = None

            if row[cursor] == '#':
                place_for_rock = None
            cursor += 1
        output.append(row)
        # print(row)
    return np.array(output)


def get_weight(plate):
    total_weight = 0
    for row in plate:
        lever = len(row)
        weight_of_row = 0
        i = 0
        while lever > 0:
            if row[i] == 'O':
                weight_of_row += lever
            lever -= 1
            i += 1
        total_weight += weight_of_row
    return total_weight


print('-- PART 1 --')

dev_plate = transpose(dev_input)
dev_plate = tilt(dev_plate)
# print(dev_plate)
# print(get_weight(dev_plate))

# input1 = get_input_data.get_input('day_14')
# the_plate = transpose(input1)
# the_plate = tilt(the_plate)
# print(get_weight(the_plate))

