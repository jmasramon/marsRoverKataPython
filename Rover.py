__author__ = 'jmasramon'

from utilityFunctions import *


class Rover:
    position = {}
    orientation = ''
    orders = ''
    navigator = None
    ORDER_DICT = {'fN': go_north, 'fS': go_south, 'fE': go_east, 'fW': go_west,
                  'bN': go_south, 'bS': go_north, 'bE': go_west, 'bW': go_east,
                  'lN': turn_west, 'lS': turn_east, 'lE': turn_north, 'lW': turn_south,
                  'rN': turn_east, 'rS': turn_west, 'rE': turn_south, 'rW': turn_north}

    def __init__(self, initial_position, initial_orientation, navigator=''):
        self.position = initial_position
        self.orientation = initial_orientation
        self.navigator = navigator

    def run_orders(self):
        for order in self.orders:
            if order in ('f', 'b'):
                self._move(order)
            elif order in ('l', 'r'):
                self._reorient(order)

    def _move(self, order):
        if not self.navigator:
            self.position = self._get_order_from_dict(order)(self.position)
        else:
            self.position = self._get_order_from_navigator(order)(self.position)

    def _get_order_from_dict(self, order):
        return self.ORDER_DICT[order + self.orientation]

    def _get_order_from_navigator(self, order):
        return getattr(self.navigator, (self._get_order_from_dict(order)).__name__)

    def _reorient(self, order):
        self.orientation = self._get_order_from_dict(order)()
