"""
This ia the A*-algorithm class. 
"""

import pygame
from queue import PriorityQueue


# This is the Manhattan distance function which calculates an estimation of
# the distance between two nodes.
def manhattan_distance(position1, position2):
        x1, y1 = position1
        x2, y2 = position2
        return abs(x1 - x2) + abs(y1 - y2)


# This method constructs/colors the path.
def construct_path(previous_node, current_node, draw):
        while current_node in previous_node:
                current_node = previous_node[current_node]
                current_node.make_path()
                draw()


# A*-algorithm
def asterisk_algo(draw, grid, start, end):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}

        # Initializing
        g_n = {node: float("inf") for row in grid for node in row}
        g_n[start] = 0

        # f_n = g_n + manhattan_distance
        f_n = {node: float("inf") for row in grid for node in row}
        f_n[start] = manhattan_distance(start.get_pos(), end.get_pos())

        open_set_hash = {start}

        # Running the algorithm after Initialization
        while not open_set.empty():
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                        
                current_node = open_set.get()[2]
                open_set_hash.remove(current_node)

                if current_node == end:
                        construct_path(came_from, end, draw)
                        end.make_end()
                        return True
                
                for neighbor in current_node.neighbors:
                       temp_g_n = g_n[current_node] + 1

                       if temp_g_n < g_n[current_node]:
                               came_from[neighbor] = current_node
                               g_n[neighbor] = temp_g_n
                               f_n[neighbor] = temp_g_n + manhattan_distance(neighbor.get_pos(), end.get_pos())
                               if neighbor not in open_set_hash:
                                       count += 1
                                       open_set.put((f_n[neighbor], count, neighbor))
                                       open_set_hash.add(neighbor)
                                       neighbor.make_open()
                
                draw()

                if current_node != start:
                        current_node.make_closed()

        return False
