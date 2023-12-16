import get_input_data

dev_input = [

    '.|...\\....',
    '|.-.\\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....'

]


def get_char_at_pos(pos, env):
    # print(pos[0])
    # print(pos[1])
    if pos[0] < 0 or pos[0] > len(env) - 1:
        return None

    if pos[1] < 0 or pos[1] > len(env[0]) - 2:
        return None

    return env[pos[0]][pos[1]]


def get_next_pos(direction, pos):
    next_pos = None

    if direction == 'N':
        next_pos = (pos[0] - 1, pos[1])
    elif direction == 'E':
        next_pos = (pos[0], pos[1] + 1)
    elif direction == 'S':
        next_pos = (pos[0] + 1, pos[1])
    elif direction == 'W':
        next_pos = (pos[0], pos[1] - 1)

    if next_pos is None:
        print("next pos none form")
        print(direction)
        print(pos)
    return next_pos


def get_next_tile(direction, current_pos, env):
    next_pos = get_next_pos(direction, current_pos)
    next_char = get_char_at_pos(next_pos, env)
    if next_char is None:
        return next_pos, None

    if (direction == 'N' or direction == 'S') and next_char == '|':
        return next_pos, '.'

    if (direction == 'E' or direction == 'W') and next_char == '-':
        return next_pos, '.'

    return next_pos, next_char


def get_ray(direction, pos, env):
    current_pos = pos
    current_char = '.'
    current_dir = direction
    pos_in_ray = []
    while current_char is not None and current_char != '-' and current_char != '|':
        pos_in_ray.append(current_pos)
        # print(current_char)
        # print(current_pos)
        current_pos, current_char = get_next_tile(current_dir, current_pos, env)

        if current_char is None:
            # out of bounds
            continue

        current_dir = get_next_dir(current_char, current_dir)

    return pos_in_ray, current_dir, current_pos, current_char


def get_next_dir(current_char, current_dir):
    if (current_char == '/' and current_dir == 'E') or (current_char == '\\' and current_dir == 'W'):
        current_dir = 'N'
    elif (current_char == '\\' and current_dir == 'E') or (current_char == '/' and current_dir == 'W'):
        current_dir = 'S'
    elif (current_char == '\\' and current_dir == 'S') or (current_char == '/' and current_dir == 'N'):
        current_dir = 'E'
    elif (current_char == '\\' and current_dir == 'N') or (current_char == '/' and current_dir == 'S'):
        current_dir = 'W'
    return current_dir


def get_next_ray_inits(pos, char, env):
    next_ray_inits = []

    if char == '|':
        ray_init = ('N', pos)
        if get_char_at_pos(get_next_pos('N', pos), env) is not None:
            next_ray_inits.append(ray_init)

        ray_init = ('S', pos)
        if get_char_at_pos(get_next_pos('S', pos), env) is not None:
            next_ray_inits.append(ray_init)

    if char == '-':
        ray_init = ('E', pos)
        if get_char_at_pos(get_next_pos('E', pos), env) is not None:
            next_ray_inits.append(ray_init)

        ray_init = ('W', pos)
        if get_char_at_pos(get_next_pos('W', pos), env) is not None:
            next_ray_inits.append(ray_init)

    return next_ray_inits


def get_locations(init_state, env):

    visited_rays = dict()
    ray_hashes = dict()

    rays_to_visit = list()

    init_char = get_char_at_pos(init_state[1], env)
    real_init_dir = get_next_dir(init_char, init_state[0])
    real_init_state = (real_init_dir, init_state[1])
    rays_to_visit.append(real_init_state)

    while len(rays_to_visit) > 0:
        ray = rays_to_visit.pop()
        pos_in_ray, end_dir, end_pos, end_char = get_ray(ray[0], ray[1], env)

        visited_rays[hash(ray)] = pos_in_ray
        ray_hashes[hash(ray)] = ray

        # print(ray)
        # visualize(pos_in_ray, env)

        next_ray_inits = get_next_ray_inits(end_pos, end_char, env)
        for next_ray in next_ray_inits:
            if not visited_rays.keys().__contains__(hash(next_ray)):
                rays_to_visit.append(next_ray)

    locations = set()
    for ray_hash, pos_in_ray in visited_rays.items():
        # print(pos_in_ray)
        for pos in pos_in_ray:
            locations.add(pos)

    return locations


def visualize(locations, env):
    for y in range(len(env)):
        line = ""
        for x in range(len(env[0])):
            if locations.__contains__((y, x)):
                line = line + "#"
            else:
                line = line + '.'
        print(line)


print('-- PART 1 --')

dev_locations = get_locations(('E', (0, 0)), dev_input)
print(len(dev_locations) + 1)
# print(dev_locations)
# visualize(dev_locations, dev_input)


v_rays = dict()
ray_h = dict()

real_input = get_input_data.get_input('day_16')
real_locations = get_locations(('E', (0, 0)), real_input)
print(len(real_locations))

print('-- PART 2 --')


def get_best_init(env):
    # North side

    max_locations = 0
    max_init = None

    for x in range(len(env[0])):
        i = ('S', (0, x))
        locations = get_locations(i, env)
        if len(locations) > max_locations:
            max_locations = len(locations)
            max_init = i

    # South side

    for x in range(len(env[0])):
        i = ('N', (len(env) - 1, x))
        locations = get_locations(i, env)
        if len(locations) > max_locations:
            max_locations = len(locations)
            max_init = i

    # East side

    for y in range(len(env)):
        i = ('W', (y, len(env[0]) - 1))
        locations = get_locations(i, env)
        if len(locations) > max_locations:
            max_locations = len(locations)
            max_init = i

    # West side

    for y in range(len(env)):
        i = ('E', (y, 0))
        locations = get_locations(i, env)
        if len(locations) > max_locations:
            max_locations = len(locations)
            max_init = i

    return max_locations, max_init


max_l, max_i = get_best_init(dev_input)
print(max_l)
print(max_i)

max_l, max_i = get_best_init(real_input)
print(max_l - 1)
print(max_i)
