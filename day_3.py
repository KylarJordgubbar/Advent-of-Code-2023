import re
from collections import Counter
from functools import reduce

import get_input_data

dev_input = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]


def pad_row(row):
    return '.' + row + '.'


def pad_input(i):
    res = list()

    res.append('.' * (len(i[0]) + 2))

    for row in i:
        res.append(pad_row(row))

    res.append('.' * (len(i[0]) + 2))

    return res


# for i in range(len(dev_input)):
#    print(dev_input[i])

# print(dev_input[1][2])


def get_total_sum(the_input):
    total_sum = 0

    for row_nr in range(len(the_input)):
        row = the_input[row_nr]
        # print(row)
        iterable = re.finditer('[\d]+', row)

        row_sum = 0

        for match in iterable:
            y_coords = list()
            x_coords = list()

            x_span = list(range(match.span()[0] - 1, match.span()[1] + 1))
            y_span = list(range(row_nr - 1, row_nr + 2))

            for y in y_span:
                for x in x_span:
                    y_coords.append(y)
                    x_coords.append(x)
                    # print(str(y)+', '+str(x))

            is_part_nr = True
            for i in range(len(y_coords)):
                if re.match('[*#$%&@/+=-]', the_input[y_coords[i]][x_coords[i]]) is not None:
                    break
            else:
                # The else block will NOT be executed if the loop is stopped by a break statement.
                is_part_nr = False

            if is_part_nr:
                row_sum = row_sum + int(match.group())

        # print(row_sum)
        total_sum = total_sum + row_sum

    return total_sum


def get_total_gear_sum(the_input):
    total_sum = 0

    gear_and_numbers = list()

    for row_nr in range(len(the_input)):
        row = the_input[row_nr]
        # print(row)
        iterable = re.finditer('[\d]+', row)

        for match in iterable:
            y_coords = list()
            x_coords = list()

            x_span = list(range(match.span()[0] - 1, match.span()[1] + 1))
            y_span = list(range(row_nr - 1, row_nr + 2))

            for y in y_span:
                for x in x_span:
                    y_coords.append(y)
                    x_coords.append(x)
                    # print(str(y)+', '+str(x))

            for i in range(len(y_coords)):
                if re.match('[*]', the_input[y_coords[i]][x_coords[i]]) is not None:
                    # print(y_coords[i] * 1000 + x_coords[i])
                    # print(int(match.group()))
                    gear_and_numbers.append(((y_coords[i] * 1000 + x_coords[i]), (int(match.group()))))

    gears = [x[0] for x in gear_and_numbers]
    for k, v in dict(Counter(gears)).items():
        if v >= 2:
            numbers = list()
            for gear, number in gear_and_numbers:
                if k == gear:
                    numbers.append(number)
            total_sum = total_sum + reduce(lambda x, y: x * y, numbers)
    return total_sum


print('-- PART 1 --')
dev_input = pad_input(dev_input)
print(get_total_sum(dev_input))

input1 = pad_input(get_input_data.get_input('day_3'))
print(get_total_sum(input1))

print('-- PART 2 --')
print(get_total_gear_sum(dev_input))
print(get_total_gear_sum(input1))
