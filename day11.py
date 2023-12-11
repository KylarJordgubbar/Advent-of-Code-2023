import get_input_data
import re
from itertools import combinations

dev_input = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....'
]


def increment_vals_over_limit(l, limit):
    res = []
    for e in l:
        if e > limit:
            res.append(e + 1)
        else:
            res.append(e)
    return res


def expand_universe_in_one_direction(vals):
    i = 0
    while i < max(vals):
        if not vals.__contains__(i):
            vals = increment_vals_over_limit(vals, i)
            i += 1
        i += 1
    return vals


def list_sort(l):
    l2 = l
    l2.sort()
    return l2


def get_galaxies(the_input):
    x_vals = []
    y_vals = []

    for y in range(len(the_input)):
        iterable = re.finditer('(#)', the_input[y])
        for i in iterable:
            x_vals.append(i.start())
            y_vals.append(y)

    y_vals = expand_universe_in_one_direction(y_vals)
    x_vals = expand_universe_in_one_direction(x_vals)

    galaxies = set()
    for i in range(len(y_vals)):
        galaxies.add((x_vals[i], y_vals[i]))
    return galaxies


def get_total(galaxies):
    c = list(combinations(galaxies, 2))
    total = 0
    for combo in c:
        a = combo[0]
        b = combo[1]
        # print(a)
        # print(b)
        delta_x = abs(a[0] - b[0])
        delta_y = abs(a[1] - b[1])
        distance = delta_y + delta_x
        # print(distance)
        total += distance
    return total


print('-- PART 1 --')

print(get_total(get_galaxies(dev_input)))
input1 = get_input_data.get_input('day_11')
print(get_total(get_galaxies(input1)))

print('-- PART 2 --')


def increment_vals_over_limit_pt2(l, limit):
    res = []
    for e in l:
        if e > limit:
            res.append(e + 1000000 - 1)
        else:
            res.append(e)
    return res


def expand_universe_in_one_direction_pt2(vals):
    i = 0
    while i < max(vals):
        if not vals.__contains__(i):
            vals = increment_vals_over_limit_pt2(vals, i)
            i += 1000000 - 1
        i += 1
    return vals


def get_galaxies_pt2(the_input):
    x_vals = []
    y_vals = []

    for y in range(len(the_input)):
        iterable = re.finditer('(#)', the_input[y])
        for i in iterable:
            x_vals.append(i.start())
            y_vals.append(y)

    y_vals = expand_universe_in_one_direction_pt2(y_vals)
    x_vals = expand_universe_in_one_direction_pt2(x_vals)

    galaxies = set()
    for i in range(len(y_vals)):
        galaxies.add((x_vals[i], y_vals[i]))
    return galaxies


dev_galaxies = get_galaxies_pt2(dev_input)

real_galaxies = get_galaxies_pt2(input1)
print(get_total(real_galaxies))
