__author__ = 'jmasramon'

from utilityFunctions import *

# TODO: abstract common control structures with higher order functions

class Navigator:
    map_size = 0
    obstacles = ()

    def go_east(self, position):
        print('entered navigator.go_east')
        temp_position = go_east(position)
        print(tuple(temp_position.values()))
        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(position, temp_position)
        elif temp_position['x'] > self.map_size:
            temp_position['x'] = -(temp_position['x']-1)
        return temp_position

    def go_west(self, position):
        print('entered navigator.go_west')
        temp_position = go_west(position)
        print(tuple(temp_position.values()))
        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(position, temp_position)
        elif temp_position['x'] < -self.map_size:
            temp_position['x'] = -(temp_position['x']+1)
        return temp_position

    def go_north(self, position):
        print('entered navigator.go_north')
        temp_position = go_north(position)
        print(tuple(temp_position.values()))
        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(position, temp_position)
        elif temp_position['y'] > self.map_size:
            temp_position['y'] = -(temp_position['y']-1)
        return temp_position

    def go_south(self, position):
        print('entered navigator.go_south')
        temp_position = go_south(position)
        print(tuple(temp_position.values()))
        if is_dic_in_dic_list(temp_position, self.obstacles):
            return report_obstacle(position, temp_position)
        elif temp_position['y'] < -self.map_size:
            temp_position['y'] = -(temp_position['y']+1)
        return temp_position
