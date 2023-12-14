import re
import get_input_data

dev_input = [
    '.....',
    '.S-7.',
    '.|.|.',
    '.L-J.',
    '.....'
]

dev_input = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...'
]


def find_start(the_input):
    res_x = 0
    res_y = 0
    do_break = True
    for y in range(len(the_input)):
        do_break = True
        line = the_input[y]
        iterable = re.finditer('(S)', the_input[y])
        for i in iterable:
            res_x = i.start()
            res_y = y
            break
        else:
            do_break = False

        if do_break:
            break

    return ((res_x, res_y))




def get_char_at(pos, the_input):
    #print(pos)
    if pos[0] < 0 or pos[0] >= len(the_input[0]) or pos[1] < 0 or pos[1] >= len(the_input):
        return '.'
    return the_input[pos[1]][pos[0]]


def has_north_connection(pos, the_input):
    c = get_char_at((pos[0], pos[1] - 1), the_input)
    if c == '|' or c == 'F' or c == '7' or c == 'S':
        return (pos[0], pos[1] - 1)
    else:
        return None


def has_south_connection(pos, the_input):
    c = get_char_at((pos[0], pos[1] + 1), the_input)
    if c == '|' or c == 'J' or c == 'L' or c == 'S':
        return (pos[0], pos[1] + 1)
    else:
        return None


def has_west_connection(pos, the_input):
    c = get_char_at((pos[0] - 1, pos[1]), the_input)
    if c == '-' or c == 'F' or c == 'L' or c == 'S':
        return (pos[0] - 1, pos[1])
    else:
        return None


def has_east_connection(pos, the_input):
    c = get_char_at((pos[0] + 1, pos[1]), the_input)
    if c == '-' or c == '7' or c == 'J' or c == 'S':
        return (pos[0] + 1, pos[1])
    else:
        return None


def is_end(pos, the_input):
    if get_char_at(pos, the_input) == 'S':
        return True
    else:
        return False


def get_next_pos(came_from, pos, the_input):
    exits = set()

    c = get_char_at(pos, the_input)

    if c == 'S':
        exits.add(has_north_connection(pos, the_input))
        exits.add(has_south_connection(pos, the_input))
        exits.add(has_east_connection(pos, the_input))
        exits.add(has_west_connection(pos, the_input))
    elif c == '|':
        exits.add(has_north_connection(pos, the_input))
        exits.add(has_south_connection(pos, the_input))
    elif c == 'F':
        exits.add(has_south_connection(pos, the_input))
        exits.add(has_east_connection(pos, the_input))
    elif c == '-':
        exits.add(has_east_connection(pos, the_input))
        exits.add(has_west_connection(pos, the_input))
    elif c == '7':
        exits.add(has_south_connection(pos, the_input))
        exits.add(has_west_connection(pos, the_input))
    elif c == 'L':
        exits.add(has_north_connection(pos, the_input))
        exits.add(has_east_connection(pos, the_input))
    elif c == 'J':
        exits.add(has_north_connection(pos, the_input))
        exits.add(has_west_connection(pos, the_input))

    # north = has_north_connection(pos, the_input)
    # south = has_south_connection(pos, the_input)
    # east = has_east_connection(pos, the_input)
    # west = has_west_connection(pos, the_input)

    # if north is not None:
    #     print("north: "+get_char_at(north, the_input))
    # if south is not None:
    #     print("south: "+get_char_at(south, the_input))
    # if east is not None:
    #     print("east: "+get_char_at(east, the_input))
    # if west is not None:
    #     print("west: "+get_char_at(west, the_input))

    if exits.__contains__(None):
        exits.remove(None)

    if exits.__contains__(came_from):
        exits.remove(came_from)

    e = None
    if len(exits) == 1 or came_from is None:
        e = exits.pop()
    elif came_from is not None:
        print("i am lost at "+str(pos)+" from "+str(came_from))

    if is_end(e, the_input):
        return None
    return e


def get_track_length(the_input):
    next_pos = find_start(the_input)

    came_from = None
    length = 0
    while next_pos is not None:
        #print(next_pos)
        new_pos = get_next_pos(came_from, next_pos, the_input)
        came_from = next_pos
        next_pos = new_pos
        length += 1

    return (length)

#print(get_track_length(dev_input)/2)

input1 = get_input_data.get_input('day_10')
#print(find_start(input1))
#get_next_pos((100, 96), (100, 96), input1)

print(get_track_length(get_input_data.get_input('day_10'))/2)