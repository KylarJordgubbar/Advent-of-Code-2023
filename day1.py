import re

import get_input_data

part1 = get_input_data.get_input('day_1')


def get_last_digit(row):
    return int(re.findall('^.*([\d]{1})', row)[0])


def get_first_digit(row):
    return int(re.findall('([\d]{1}).*$', row)[0])


def get_row_value(row):
    return get_first_digit(row) * 10 + get_last_digit(row)


def get_sum_of_rows(rows):
    total_sum = 0

    for row in rows:
        total_sum = total_sum + get_row_value(row)

    return total_sum


print(get_sum_of_rows(part1))


def pre_process(row):
    row = row.replace('one', 'o1e')
    row = row.replace('two', 't2o')
    row = row.replace('three', 't3e')
    row = row.replace('four', 'f4r')
    row = row.replace('five', 'f5v')
    row = row.replace('six', 's6x')
    row = row.replace('seven', 's7n')
    row = row.replace('eight', 'e8t')
    row = row.replace('nine', 'n9e')
    return row


def get_sum_of_rows_part_2(rows):
    total_sum = 0

    for row in rows:
        total_sum = total_sum + get_row_value(pre_process(row))

    return total_sum


print(get_sum_of_rows_part_2(part1))
