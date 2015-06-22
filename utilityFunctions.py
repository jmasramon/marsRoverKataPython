__author__ = 'jmasramon'


def go_east(position):
    return {'x': position['x'] + 1, 'y': position['y']}


def go_west(position):
    return {'x': position['x'] - 1, 'y': position['y']}


def go_north(position):
    print('entered go_north with position:', position)
    return {'x': position['x'], 'y': position['y'] + 1}


def go_south(position):
    return {'x': position['x'], 'y': position['y'] - 1}


def turn_east():
    return 'E'


def turn_west():
    return 'W'


def turn_north():
    return 'N'


def turn_south():
    return 'S'


def report_obstacle(position, temp_position):
    position["obstacle"] = temp_position
    return position


def is_same_tuple(t1, t2):
    return t1 == t2


def is_same_dictionary(d1, d2):
    return len(set(d1.items()) & set(d2.items())) == len(d1)


def is_dic_in_dic_list(d, dl):
    for dd in dl:
        if (len(set(d.items()) & set(dd.items()))) >= 2:
            return True
    return False
