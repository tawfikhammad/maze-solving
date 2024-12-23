from collections import deque
from queue import PriorityQueue
from constants import grid_size


# BFS algorithm 
def bfs(maze, start, goal):
    visited = set()                 # tracking visited nodes
    queue = deque([[start]])        # queue stores the current paths being explored
    
    while queue:
        path = queue.popleft()      # return and remove the last path of queue
        x, y = path[-1]  

        yield path

        # If the goal is reached, return the path
        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            
            # Explore 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                nx, ny = x + dx, y + dy

                # check it lies within the boundaries and free cell
                if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[ny][nx] == 0:  
                    new_path = list(path)
                    new_path.append((nx, ny))
                    queue.append(new_path)
    
# DFS algorithm (stack-based approach)
def dfs(maze, start, goal):
    visited = set()                 
    stack = [[start]]               
     
    while stack:
        path = stack.pop()
        x, y = path[-1]

        yield path
        
        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            
            # Explore 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[ny][nx] == 0:
                    new_path = list(path)
                    new_path.append((nx, ny))
                    stack.append(new_path)
    

# reconstruct the path from came_from 
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]  # Return reversed path

# A* algorithm 
def a_star(maze, start, goal):
    open_set = set([start])     # Set of nodes to be evaluated
    g_score = {start: 0}        # store the cost to reach a node
    f_score = {start: heuristic(start, goal)}  # f = g + h
    came_from = {}  
    
    while open_set:
        current = min(open_set, key=lambda x: f_score.get(x, float('inf')))  # Get node with lowest f_score
        
        # If goal is reached, reconstruct the path
        if current == goal:
            yield  reconstruct_path(came_from, current)
        
        open_set.remove(current)
        x, y = current
        
        # Explore 4 directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[ny][nx] == 0:
                tentative_g_score = g_score[current] + 1
                
                # If this path is better, update scores and add node to open set
                if (nx, ny) not in g_score or tentative_g_score < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = (x, y)
                    g_score[(nx, ny)] = tentative_g_score
                    f_score[(nx, ny)] = tentative_g_score + heuristic((nx, ny), goal)
                    open_set.add((nx, ny))
    
# Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# UCS algorithm 
def ucs(maze, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))  
    visited = set()
    came_from = {}
    cost_so_far = {start: 0}
    
    while not queue.empty():
        current_cost, current = queue.get()
        
        if current == goal:
            yield reconstruct_path(came_from, current)
        
        if current in visited:
            continue
        
        visited.add(current)
        x, y = current
        
        # Explore 4 neighboring directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[ny][nx] == 0:
                new_cost = current_cost + 1
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    priority = new_cost
                    queue.put((priority, (nx, ny)))
                    came_from[(nx, ny)] = (x, y)
    


