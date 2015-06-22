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

# TODO: make tests independent of one another (the test framework does not have a before())
# TODO: refactor tests following "effective unit testing" best practices

from Navigator import *
from Rover import *

CARDINAL_POINTS = ('N', 'S', 'E', 'W')

with given.a_rover:
    x = 0
    y = 0
    starting_point = {'x': x, 'y': y}
    initial_direction = 'N'
    rover = Rover(starting_point, initial_direction)

    the(isinstance(rover, Rover)).should.be(True)

    with when.supplied_the_starting_point:
        with then.the_starting_point_should_have_two_axis:
            the(starting_point).should.contain('x')
            the(starting_point).should.contain('y')

        with then.the_initial_direction_should_belong_to_NSEW:
            the(initial_direction in CARDINAL_POINTS).should.be(True)

    with when.supplied_with_a_character_command:
        with and_.the_rover_should_give_current_position:
            the(rover.position).should.be(starting_point)

        with and_.the_rover_should_give_current_orientation:
            the(rover.orientation).should.be('N')

        with and_.the_rover_should_accept_f_command_and_go_forward:
            rover.orders = 'f'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 1})).should.be(True)
            the(rover.orientation).should.be('N')

        with and_.the_rover_should_accept_b_command_and_go_backward:
            rover.orders = 'b'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 0})).should.be(True)
            the(rover.orientation).should.be('N')

        with and_.the_rover_should_accept_l_command_and_orient_left:
            rover.orders = 'l'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 0})).should.be(True)
            the(rover.orientation).should.be('W')

        with and_.the_rover_should_accept_r_command_and_orient_right:
            rover.orders = 'r'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 0})).should.be(True)
            the(rover.orientation).should.be('N')

    with when.supplied_with_a_character_array_of_commands:
        with then.the_rover_should_do_as_commanded:
            rover.orders = 'flf'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': -1, 'y': 1})).should.be(True)
            the(rover.orientation).should.be('W')

            rover.orders = 'brb'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 0})).should.be(True)
            the(rover.orientation).should.be('N')

            rover.orders = 'flflflfl'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': 0})).should.be(True)
            the(rover.orientation).should.be('N')

    with when.supplied_with_a_navigator:
        navigator = Navigator()
        MAP_SIZE = 3
        navigator.map_size = MAP_SIZE
        rover = Rover(starting_point, initial_direction, navigator)

        with then.the_rover_should_wrap_from_the_upper_edge:
            rover.orders = 'ffff'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': -MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_lower_edge:
            rover.orders = 'b'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': 0, 'y': MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_left_edge:
            rover.orders = 'lffff'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': MAP_SIZE, 'y': MAP_SIZE})).should.be(True)

        with and_.the_rover_should_wrap_from_the_right_edge:
            rover.orders = 'rrf'
            rover.run_orders()
            print(rover.position)
            the(is_same_dictionary(rover.position, {'x': -MAP_SIZE, 'y': MAP_SIZE})).should.be(True)

    with when.supplied_with_obstacles:
        obstacles = ({'x': 1, 'y': 1}, {'x': -1, 'y': 2}, {'x': -2, 'y': -2}, {'x': -2, 'y': -MAP_SIZE})
        navigator.obstacles = obstacles
        rover = Rover(starting_point, initial_direction, navigator)

        with then.the_rover_should_avoid_them:
            with and_.the_rover_goes_to_the_E:
                rover.orders = 'frfff'
                rover.run_orders()
                print(rover.position)
                the(rover.position['x']).should.be(0)
                the(rover.position['y']).should.be(1)
                the(is_same_dictionary(rover.position['obstacle'], {'x': 1, 'y': 1})).should.be(True)
                the(rover.orientation).should.be('E')

            with and_.the_rover_goes_to_the_W:
                rover.orders = 'lflfff'
                rover.run_orders()
                print(rover.position)
                the(rover.position['x']).should.be(0)
                the(rover.position['y']).should.be(2)
                the(is_same_dictionary(rover.position['obstacle'], {'x': -1, 'y': 2})).should.be(True)
                the(rover.orientation).should.be('W')

            with and_.the_rover_goes_to_the_S:
                rover.orders = 'lfrfflfffff'
                rover.run_orders()
                print(rover.position)
                the(rover.position['x']).should.be(-2)
                the(rover.position['y']).should.be(-1)
                the(is_same_dictionary(rover.position['obstacle'], {'x': -2, 'y': -2})).should.be(True)
                the(rover.orientation).should.be('S')

            with and_.the_rover_goes_to_the_N:
                rover.orders = 'lflfffff'
                rover.run_orders()
                print(rover.position)
                the(rover.position['x']).should.be(-1)
                the(rover.position['y']).should.be(1)
                the(is_same_dictionary(rover.position['obstacle'], {'x': -1, 'y': 2})).should.be(True)
                the(rover.orientation).should.be('N')
