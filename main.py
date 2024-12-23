import pygame
from constants import BACKGROUND_COLOR, END_COLOR, width, height
from maze import generate_maze, draw_maze
from pathfinding import bfs, dfs, a_star, ucs

def select_algorithm():
    print("Select an algorithm:")
    print("1. BFS")
    print("2. DFS")
    choice = input("Enter the number: ")
    return {"1": bfs, "2": dfs}.get(choice, bfs)

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    maze = generate_maze()
    start, goal = (1, 1), (28, 28)
    selected_algorithm = select_algorithm()

    running = True
    path_generator = selected_algorithm(maze, start, goal) 
    path = []

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_maze(screen, maze)
        
        # Update path step-by-step
        try:
            path = next(path_generator)  # Get the next step
        except StopIteration:
            pass  # completed

        # Draw the current path
        for x, y in path:
            pygame.draw.rect(screen, END_COLOR, (x * 20, y * 20, 20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
