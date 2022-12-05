# 27/05/2021
# A*Star Pathfinder

import pygame
import time
import sys
from win32api import GetSystemMetrics
import math
from queue import PriorityQueue

import pygame

# Color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (244, 226, 198)
LIGHT_SLATE_GRAY = (119, 136, 153)
BLUE = (0, 0, 255)
GREEN = (124, 252, 0)
MAGENTA = (255, 0, 144)
YELLOW = (255, 255, 0)

# Screen resolution
WIDTH = GetSystemMetrics(0) // 3
HEIGHT = GetSystemMetrics(1) // 3

# Grid size
RATIO = 14
NUM_OF_GRID = 12
PIX_GRID_SIZE = HEIGHT / RATIO

CENTER_OF_SCREEN_X = WIDTH / 2
TOP_LEFT_BLOCK_X = CENTER_OF_SCREEN_X - PIX_GRID_SIZE * (NUM_OF_GRID / 2)
TOP_LEFT_BLOCK_Y = HEIGHT / RATIO * ((RATIO - NUM_OF_GRID) / 2) - NUM_OF_GRID

TOP_LEFT_BLOCK_POS = [TOP_LEFT_BLOCK_X, TOP_LEFT_BLOCK_Y]

BLOCK_SIZE = PIX_GRID_SIZE / 10 * 8
WIDTH_HEIGHT = (BLOCK_SIZE, BLOCK_SIZE)

# Pygame Frame
FRAME = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")
FRAME.fill(BEIGE)

# Logic table Flag
EMPTY_FLAG = 0
WALL_FLAG = 1
SRC_FLAG = 2
DST_FLAG = 3

# Invalid flags
INVALID_FLAG = -1
INVALID_BLOCK_SELECTED_FLAG = [-1, -1]
INVALID_INDEX = [-1, -1]
NO_VALID_ROUTE_FLAG = "-1"

# Block colors
SRC_NODE_COLOR = RED
DST_NODE_COLOR = GREEN
EMPTY_NODE_COLOR = WHITE
WALL_NODE_COLOR = LIGHT_SLATE_GRAY
SEARCH_NODE_COLOR = BLUE
SUCCESSFUL_ROUTE_COLOR = YELLOW
OPEN_NODE_COLOR = (0, 0, 0) # TEMP
CLOSE_NODE_COLOR = (0, 0, 0) # TEMP

class Node:
    def __init__(self, row, column):
        """Give row and column in terms of grid index"""

        self.row = TOP_LEFT_BLOCK_X + row * PIX_GRID_SIZE
        self.column = TOP_LEFT_BLOCK_Y + column * PIX_GRID_SIZE
        self.color = EMPTY_NODE_COLOR

    def is_node_this_color(self, color) -> bool:
        """Return if node is input color"""

        return self.color == color

    def return_node_location(self) -> tuple:
        """Return node location"""

        return (self.row, self.column)

    def set_node_color(self, color: tuple):
        """Set the color of the node"""

        self.color = color

    def draw_node(self):
        """Draw the node"""

        pygame.draw.rect(FRAME, self.color, ((self.row, self.column), WIDTH_HEIGHT))
        pygame.display.update()

    def update_neighbour(self, grid: list):
        try:
            if grid[self.row - 1][self.column - 1].is_node_this_color(OPEN_NODE_COLOR): # Top Left
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row][self.column - 1].is_node_this_color(OPEN_NODE_COLOR): # Top
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row + 1][self.column - 1].is_node_this_color(OPEN_NODE_COLOR): # Top Right
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row - 1][self.column].is_node_this_color(OPEN_NODE_COLOR): # Left
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row + 1][self.column].is_node_this_color(OPEN_NODE_COLOR): # Right
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row - 1][self.column + 1].is_node_this_color(OPEN_NODE_COLOR): # Bottom Left
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row][self.column + 1].is_node_this_color(OPEN_NODE_COLOR): # Bottom
                # ADD TO OPEN
                pass
        except IndexError:
            pass
        try:
            if grid[self.row + 1][self.column + 1].is_node_this_color(OPEN_NODE_COLOR): # Bottom Right
                # ADD TO OPEN
                pass
        except IndexError:
            pass


def generate_grid() -> list:
    """Create and draw grid"""

    grid = []
    for row in range(NUM_OF_GRID):
        grid.append([])
        for column in range(NUM_OF_GRID):
            grid[row].append(Node(row, column))
            grid[row][column].draw_node()
    return grid


def get_clicked_position(row: float, column: float) -> tuple:
    """Return clicked position in terms of grid number: (row, column)"""

    row -= TOP_LEFT_BLOCK_X
    column -= TOP_LEFT_BLOCK_Y

    node_row = row // PIX_GRID_SIZE
    node_column = column // PIX_GRID_SIZE

    return int(node_row), int(node_column)


def pathfind(src_node, dst_node):
    """pAThfInDUr"""

    count = 0
    open_set = PriorityQueue()
    open_set_hash = {src_node}
    open_set.put((0, count, src_node))
    came_from = {}
    g_score = 0
    f_score = 0 # heuristic?

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == dst_node:
                pass

            for neighbour in current.neighbors:
                pass



def main():
    grid = generate_grid()
    src_dst_node_state = [False, False]
    src_node_state = src_dst_node_state[0]
    dst_node_state = src_dst_node_state[1]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if pygame.mouse.get_pressed()[0]: # LEFT
                row, column = pygame.mouse.get_pos()

                # Click was within grid
                if TOP_LEFT_BLOCK_X < row < TOP_LEFT_BLOCK_X + NUM_OF_GRID * PIX_GRID_SIZE:
                    if TOP_LEFT_BLOCK_Y < column < TOP_LEFT_BLOCK_Y + NUM_OF_GRID * PIX_GRID_SIZE:
                        node_row, node_column = get_clicked_position(row, column)
                        node = grid[node_row][node_column]

                        # If blank
                        if node.is_node_this_color(EMPTY_NODE_COLOR):

                            # Check for source and destination node presences
                            if src_node_state == False:
                                color = SRC_NODE_COLOR
                                src_node_state = True
                            elif dst_node_state == False:
                                color = DST_NODE_COLOR
                                dst_node_state = True
                            else:
                                color = WALL_NODE_COLOR

                            node.set_node_color(color)
                            node.draw_node()

            if pygame.mouse.get_pressed()[2]: # RIGHT
                row, column = pygame.mouse.get_pos()

                # Click was within grid
                if TOP_LEFT_BLOCK_X < row < TOP_LEFT_BLOCK_X + NUM_OF_GRID * PIX_GRID_SIZE:
                    if TOP_LEFT_BLOCK_Y < column < TOP_LEFT_BLOCK_Y + NUM_OF_GRID * PIX_GRID_SIZE:
                        node_row, node_column = get_clicked_position(row, column)
                        node = grid[node_row][node_column]

                        if node.is_node_this_color(SRC_NODE_COLOR):
                            src_node = node
                            src_node_state = False
                        elif node.is_node_this_color(DST_NODE_COLOR):
                            dst_node = node
                            dst_node_state = False

                        # Check for source and destination node presences
                        node.set_node_color(EMPTY_NODE_COLOR)
                        node.draw_node()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if src_node_state and dst_node_state:
                        pathfind(src_node, dst_node)

                if event.key == pygame.K_SPACE:
                    grid = generate_grid()
                    src_dst_node_state = [False, False]
                    src_node_state = src_dst_node_state[0]
                    dst_node_state = src_dst_node_state[1]


if __name__ == "__main__":
    main()
