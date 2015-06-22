__author__ = 'jmasramon'

from utilityFunctions import *

# TODO: abstract common control structures with higher order functions

class Rover:
    position = {}
    orientation = ''
    orders = ''
    navigator = None

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
