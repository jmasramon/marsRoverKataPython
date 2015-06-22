__author__ = 'jmasramon'

from utilityFunctions import *
import utilityFunctions

# TODO: abstract common control structures with higher order functions


def wrap_east(temp_position):
    wrap(temp_position, 'x', lambda x: -(x - 1))


def wrap_west(temp_position):
    wrap(temp_position, 'x', lambda x: -(x + 1))


def wrap_north(temp_position):
    wrap(temp_position, 'y', lambda x: -(x - 1))


def wrap_south(temp_position):
    wrap(temp_position, 'y', lambda x: -(x + 1))


def wrap(temp_postion, axis, wrap_algorithm):
    temp_postion[axis] = wrap_algorithm(temp_postion[axis])


class Navigator:
    map_size = 0
    obstacles = ()

    def go_east(self, initial_position):
        return self.go_somewhere(initial_position, 'east', self.needs_east_wrapping, wrap_east)

    def go_west(self, initial_position):
        return self.go_somewhere(initial_position, 'west', self.needs_west_wrapping, wrap_west)

    def go_north(self, initial_position):
        return self.go_somewhere(initial_position, 'north', self.needs_north_wrapping, wrap_north)

    def go_south(self, initial_position):
        return self.go_somewhere(initial_position, 'south', self.needs_south_wrapping, wrap_south)

    def go_somewhere(self, position, direction, predicate, action):
        method_to_call = getattr(utilityFunctions, "go_" + direction)
        temp_position = method_to_call(position)

        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(position, temp_position)
        elif predicate(temp_position):
            action(temp_position)

        return temp_position

    #########################################################

    def needs_east_wrapping(self, temp_position):
        return temp_position['x'] > self.map_size

    def needs_west_wrapping(self, temp_position):
        return temp_position['x'] < -self.map_size

    def needs_north_wrapping(self, temp_position):
        return temp_position['y'] > self.map_size

    def needs_south_wrapping(self, temp_position):
        return temp_position['y'] < -self.map_size
