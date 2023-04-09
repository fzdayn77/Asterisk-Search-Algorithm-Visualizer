"""
This class defines the characteristics of each node/square:
                color/state, position, handling the drawing of nodes.
"""

import pygame

# Colors
ORANGE = (255, 165 ,0)      # Start
TURQUOISE = (64, 224, 208)  # End
YELLOW = (255, 255, 0)      # Path

RED = (255, 0, 0)    # Closed nodes
GREEN = (0, 255, 0)  # Open nodes

WHITE = (255, 255, 255)  # Default color
BLACK = (0, 0, 0)        # Obstacle
GREY = (128, 128, 128)   # Grid-gap color


class Node:
        def __init__(self, row, col, width, total_rows):
                self.row = row
                self.col = col
                self.width = width
                self.total_rows = total_rows
                self.color = WHITE
                self.neighbors = list()
                self.x = row * width
                self.y = col * width

        def get_pos(self):
                return self.row, self.col
        
        # Checking state(=color) of the node
        def is_closed(self): return self.color == RED

        def is_open(self): return self.color == GREEN

        def is_obstacle(self): return self.color == BLACK

        def is_start(self): return self.color == ORANGE

        def is_end(self): return self.color == TURQUOISE

        # Updatiing state(=color) of the node
        def reset_all(self):
                self.color = WHITE

        def make_start(self):
                self.color = ORANGE

        def make_end(self):
                self.color = TURQUOISE

        def make_open(self):
                self.color = GREEN

        def make_closed(self):
                self.color = RED

        def make_obstacle(self):
                self.color = BLACK

        def make_path(self):
                self.color = YELLOW

        # Drawing the node as a square
        def draw_node(self, win):
                pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        # This adds all current node neighbors to the neighbirs-list.
        def update_neighbors(self, grid):
                self.neighbors = list()

                go_down = self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle()
                go_up = self.row > 0 and not grid[self.row - 1][self.col].is_obstacle()
                go_left = self.col > 0 and not grid[self.row][self.col - 1].is_obstacle()
                go_right = self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle()

                if go_down:
                        self.neighbors.append(grid[self.row + 1][self.col])
                if go_up:
                         self.neighbors.append(grid[self.row - 1][self.col])
                if go_right:
                        self.neighbors.append(grid[self.row][self.col + 1])
                if go_left:
                         self.neighbors.append(grid[self.row][self.col - 1])              
        
        def __lt__(self, other):
                return False
