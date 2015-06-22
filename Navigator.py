__author__ = 'jmasramon'

from utilityFunctions import *
import utilityFunctions

# TODO: abstract common control structures with higher order functions

class Navigator:
    map_size = 0
    obstacles = ()

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
