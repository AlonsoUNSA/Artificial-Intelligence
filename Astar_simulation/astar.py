import heapq
from settings import BLUE, CYAN, YELLOW, GRAY

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(grid, node):
    neighbors = []
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r, c = node[0] + dr, node[1] + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
            neighbors.append((r, c))
    return neighbors

def astar(grid, start, end, draw_cell):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    open_set_hash = {start}
    closed_set = set()

    while open_set:
        current = heapq.heappop(open_set)[1]
        open_set_hash.remove(current)

        # Nodo actual evaluado (amarillo)
        draw_cell(current[0], current[1], YELLOW)
        yield

        if current == end:
            # Reconstruir camino (azul)
            while current in came_from:
                current = came_from[current]
                draw_cell(current[0], current[1], BLUE)
                yield
            return

        closed_set.add(current)
        # Nodo cerrado evaluado (gris)
        draw_cell(current[0], current[1], GRAY)
        yield

        for neighbor in get_neighbors(grid, current):
            if neighbor in closed_set:
                continue

            temp_g_score = g_score[current] + 1

            if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, end)

                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)
                    # Vecino probado (cian)
                    draw_cell(neighbor[0], neighbor[1], CYAN)
                    yield
