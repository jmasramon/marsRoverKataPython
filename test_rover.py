__author__ = 'jmasramon'

from pyspecs import given, when, then, and_, the

# Develop an api that moves a rover around on a grid.
#
# You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
#
# The rover receives a character array of commands.
#
# Implement commands that move the rover forward/backward (f,b).
#
# Implement commands that turn the rover left/right (l,r).
#
# Implement wrapping from one edge of the grid to another. (planets are spheres after all)
#
# Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle,
# the rover moves up to the last possible point and reports the obstacle.

# TODO: make tests independent of one another resetting the position and orientation (the test framework does not have a before()
# TODO: abstract common control structures with higher order functions
# TODO: separate tests from productions code
# TODO: refactor tests

def go_east(position):
    return {'x': position['x'] + 1, 'y': position['y']}

def go_west(position):
    return {'x': position['x'] - 1, 'y': position['y']}

def go_north(position):
    # print('entered go_north')
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

class Navigator:
    # map = ''
    map_size = 0

    # def setMap(self, lowerLefCorner, upperRightCorner):
    def setMap(self, map_size):
        # self.map = (lowerLefCorner, upperRightCorner)
        # self.map_size = upperRightCorner[0]
        self.map_size = map_size

    def go_east(self, position):
        # print('entered navigator.go_north')
        temp_position = go_east(position)
        if temp_position['x'] > self.map_size:
            temp_position['x'] = -(temp_position['x']-1)
        return temp_position

    def go_west(self, position):
        # print('entered navigator.go_north')
        temp_position = go_west(position)
        if temp_position['x'] < -self.map_size:
            temp_position['x'] = -(temp_position['x']+1)
        return temp_position

    def go_north(self, position):
        # print('entered navigator.go_north')
        temp_position = go_north(position)
        if temp_position['y'] > self.map_size:
            temp_position['y'] = -(temp_position['y']-1)
        return temp_position

    def go_south(self, position):
        # print('entered navigator.go_north')
        temp_position = go_south(position)
        if temp_position['y'] < -self.map_size:
            temp_position['y'] = -(temp_position['y']+1)
        return temp_position



class Rover:
    position = ''
    orientation = ''
    orders = ''
    navigator = ''

    def __init__(self, initial_position, initial_orientation, navigator = ''):
        self.position = initial_position
        self.orientation = initial_orientation
        self.navigator = navigator

    def set_orders(self, new_orders):
        self.orders = new_orders

    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation

    def run_orders(self):
        order_dict = {'fN': go_north, 'fS': go_south, 'fE': go_east, 'fW': go_west,
                      'bN': go_south, 'bS': go_north, 'bE': go_west, 'bW': go_east,
                      'lN': turn_west, 'lS': turn_east, 'lE': turn_north, 'lW': turn_south,
                      'rN': turn_east, 'rS': turn_west, 'rE': turn_south, 'rW': turn_north}

        for order in self.orders:
            if order in ('f','b'):
                if not self.navigator:
                    # print('navigator not detected')
                    self.position = order_dict[order + self.orientation](self.position)
                else:
                    # print('navigator detected')
                    # print(getattr(self.navigator, (order_dict[order + self.orientation]).__name__))
                    self.position = getattr(self.navigator, (order_dict[order + self.orientation]).__name__)(self.position)
            elif order in ('l', 'r'):
                self.orientation = order_dict[order + self.orientation]()



cardinal_points = ('N', 'S', 'E', 'W')


def is_same_tuple(t1, t2):
    return sorted(t1) == sorted(t2)


def is_same_dictionary(d1, d2):
    return len(set(d1.items()) & set(d2.items())) == len(d1)


with given.a_rover:
    x = 0
    y = 0
    starting_point = {'x': x, 'y': y}
    initial_direction = 'N'
    rover = Rover(starting_point, initial_direction)

    assert is_same_tuple((1, 2), (1, 2)) is True
    assert is_same_tuple((1, 2), (3, 4)) is False
    # print(is_same_dictionary({'x': 0, 'y': 1}, {'x': 0, 'y': 1}))

    the(isinstance(rover, Rover)).should.be(True)

    with when.supplied_the_starting_point:
        with then.the_starting_point_should_have_two_axis:
            the(starting_point).should.contain('x')
            the(starting_point).should.contain('y')

        with then.the_initial_direction_should_belong_to_NSEW:
            the(initial_direction in cardinal_points).should.be(True)

    with when.supplied_with_a_character_command:
        with then.the_rover_should_accept_it:
            the(callable(getattr(rover, 'set_orders'))).should.be(True)

        with and_.the_rover_should_give_current_position:
            the(callable(getattr(rover, 'get_position'))).should.be(True)
            the(rover.get_position()).should.be(starting_point)

        with and_.the_rover_should_give_current_orientation:
            the(callable(getattr(rover, 'get_orientation'))).should.be(True)
            the(rover.get_orientation()).should.be('N')

        with and_.the_rover_should_accept_f_command_and_go_forward:
            rover.set_orders('f')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 1})).should.be(True)
            the(rover.get_orientation()).should.be('N')

        with and_.the_rover_should_accept_b_command_and_go_backward:
            rover.set_orders('b')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 0})).should.be(True)
            the(rover.get_orientation()).should.be('N')

        with and_.the_rover_should_accept_l_command_and_orient_left:
            rover.set_orders('l')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 0})).should.be(True)
            the(rover.get_orientation()).should.be('W')

        with and_.the_rover_should_accept_r_command_and_orient_right:
            rover.set_orders('r')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 0})).should.be(True)
            the(rover.get_orientation()).should.be('N')

    with when.supplied_with_a_character_array_of_commands:
        with then.the_rover_should_do_as_commanded:
            rover.set_orders('flf')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': -1, 'y': 1})).should.be(True)
            the(rover.get_orientation()).should.be('W')

            rover.set_orders('brb')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 0})).should.be(True)
            the(rover.get_orientation()).should.be('N')

            rover.set_orders('flflflfl')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': 0})).should.be(True)
            the(rover.get_orientation()).should.be('N')

    with when.supplied_with_a_navigator:
        navigator = Navigator()
        # navigator.setMap((-3,-3), (3,3))
        MAP_SIZE = 3
        navigator.setMap(MAP_SIZE)
        rover = Rover(starting_point, initial_direction, navigator)

        with and_.the_rover_should_wrap_from_the_upper_edge:
            rover.set_orders('ffff')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': -MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_lower_edge:
            rover.set_orders('b')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': 0, 'y': MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_left_edge:
            rover.set_orders('lffff')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': MAP_SIZE, 'y': MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_right_edge:
            rover.set_orders('rrf')
            rover.run_orders()
            print(rover.get_position())
            the(is_same_dictionary(rover.get_position(), {'x': -MAP_SIZE, 'y': MAP_SIZE})).should.be(True)

