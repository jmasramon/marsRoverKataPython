__author__ = 'jmasramon'

from pyspecs import given

from utilityFunctions import *

with given.utility_functions:
    assert is_same_tuple((1, 2), (1, 2)) is True
    assert is_same_tuple((1, 2), (3, 4)) is False
    assert is_same_dictionary({'x': 0, 'y': 1}, {'x': 0, 'y': 1}) is True
    assert is_same_dictionary({'x': 0, 'y': 1}, {'x': 1, 'y': 1}) is False
    assert is_dic_in_dic_list({'x': -1, 'y': 2}, ({'x': 1, 'y': 1}, {'x': -1, 'y': 2}, {'x': -2, 'y': -2})) is True
    assert is_dic_in_dic_list({'x': 0, 'y': 1}, ({'x': 1, 'y': 1}, {'x': -1, 'y': 2}, {'x': -2, 'y': -2})) is False
