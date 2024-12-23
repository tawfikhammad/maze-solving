import random
import pygame
from constants import GRID_COLOR, HIGHLIGHT_COLOR, grid_size, cell_size

# Generate the maze using depth-first search algorithm
def generate_maze():
    maze = [[1] * grid_size for _ in range(grid_size)]
    start, goal = (1, 1), (grid_size - 2, grid_size - 2)
    maze[start[1]][start[0]], maze[goal[1]][goal[0]] = 0, 0

    stack = [start]
    while stack:
        x, y = stack[-1]
        neighbors = []
        # Check available neighbors for maze carving (only vertical and horizontal)
        if x > 1 and maze[y][x - 2] == 1:
            neighbors.append((x - 2, y))

        if x < grid_size - 2 and maze[y][x + 2] == 1:
            neighbors.append((x + 2, y))

        if y > 1 and maze[y - 2][x] == 1:
            neighbors.append((x, y - 2))

        if y < grid_size - 2 and maze[y + 2][x] == 1:
            neighbors.append((x, y + 2))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[ny][nx] = 0
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()
    return maze

def draw_maze(screen, maze):
    for y in range(grid_size):
        for x in range(grid_size):
            color = GRID_COLOR if maze[y][x] == 1 else HIGHLIGHT_COLOR
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
