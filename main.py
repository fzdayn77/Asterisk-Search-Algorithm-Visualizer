import pygame
from node import Node
from node import GREY, WHITE
from asterisk_algorithm import asterisk_algo

# Constants
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* - Search Algorith Visualizer")


# This method makes the grid as 2-dimensional array and filling it with the
# nodes(considering the position, color, width).
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

# THis method draws the grey lines(horizontal and vertical) separating the nodes/squares.
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))  # horizontal lines
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))  # vertical lines

# This method draws the whole grid. 
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw_node(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

# This method returns the mouse position considering the displayed grid on the screen.
def get_mouse_position(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 60
    GRID = make_grid(ROWS, width)

    start = None
    end = None

    is_running = True
    while is_running:
        draw(win, GRID, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if pygame.mouse.get_pressed()[0]:  # LEFT-mouse-button is pressed
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_position(pos, ROWS, width)
                try:
                    node = GRID[row][col]
                except:
                    pass
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_obstacle()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT-mouse-button is pressed --> Reset the clicked node/square
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_position(pos, ROWS, width)
                try:
                    node = GRID[row][col]
                except:
                    pass
                node.reset_all()
                if node == start:
                    start = None
                if node == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in GRID:
                        for node in row:
                            node.update_neighbors(GRID)
                    
                    asterisk_algo(lambda: draw(win, GRID, ROWS, width), GRID, start, end)
                
                if event.key == pygame.K_r:  # Pressing the r-key resets everything to default state
                    start = None
                    end = None
                    GRID = make_grid(ROWS, width)

    
    pygame.quit()


# Executing
main(WIN, WIDTH)


