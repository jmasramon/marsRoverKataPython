__author__ = 'jmasramon'

from utilityFunctions import *
import utilityFunctions


class Navigator:
    def __init__(self, map_size=0, obstacles=()):
        self.map_size = map_size
        self.obstacles = obstacles

    def go_east(self, initial_position):
        return self._go_somewhere(initial_position, 'east', self._needs_east_wrapping, wrap_east)

    def go_west(self, initial_position):
        return self._go_somewhere(initial_position, 'west', self._needs_west_wrapping, wrap_west)

    def go_north(self, initial_position):
        return self._go_somewhere(initial_position, 'north', self._needs_north_wrapping, wrap_north)

    def go_south(self, initial_position):
        return self._go_somewhere(initial_position, 'south', self._needs_south_wrapping, wrap_south)

    def _go_somewhere(self, initial_position, direction, wrapping_predicate, wrapping_action):
        method_to_call = getattr(utilityFunctions, "go_" + direction)
        temp_position = method_to_call(initial_position)

        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(initial_position, temp_position)
        elif wrapping_predicate(temp_position):
            wrapping_action(temp_position)

        return temp_position

    def _needs_east_wrapping(self, temp_position):
        return temp_position['x'] > self.map_size

    def _needs_west_wrapping(self, temp_position):
        return temp_position['x'] < -self.map_size

    def _needs_north_wrapping(self, temp_position):
        return temp_position['y'] > self.map_size

    def _needs_south_wrapping(self, temp_position):
        return temp_position['y'] < -self.map_size


wrap_positive_direction = lambda x: -(x - 1)
wrap_negative_direction = lambda x: -(x + 1)


def wrap_east(temp_position):
    wrap(temp_position, 'x', wrap_positive_direction)


def wrap_west(temp_position):
    wrap(temp_position, 'x', wrap_negative_direction)


def wrap_north(temp_position):
    wrap(temp_position, 'y', wrap_positive_direction)


def wrap_south(temp_position):
    wrap(temp_position, 'y', wrap_negative_direction)


def wrap(temp_position, axis, wrap_algorithm):
    temp_position[axis] = wrap_algorithm(temp_position[axis])
