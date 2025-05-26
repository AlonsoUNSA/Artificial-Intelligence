import pygame
from grid import Grid
from settings import GREEN, RED
from astar import astar

def main():
    pygame.init()
    grid = Grid("map.csv")

    HEIGHT = grid.rows * grid.cell_size
    WIDTH = grid.cols * grid.cell_size

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación A*")

    start_pos = None
    end_pos = None
    astar_generator = None

    def draw_cell(row, col, color):
        # No dibujar aquí, sólo guardar color en el grid
        grid.color_cell(row, col, color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // grid.cell_size
                row = mouse_y // grid.cell_size

                if start_pos is None:
                    start_pos = (row, col)
                    print(f"Inicio marcado en: {start_pos}")
                elif end_pos is None and (row, col) != start_pos:
                    end_pos = (row, col)
                    print(f"Final marcado en: {end_pos}")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_pos and end_pos:
                    astar_generator = astar(grid.grid, start_pos, end_pos, draw_cell)

        if astar_generator:
            try:
                next(astar_generator)
            except StopIteration:
                astar_generator = None

        window.fill((255, 255, 255))
        grid.draw(window)

        if start_pos:
            pygame.draw.rect(window, GREEN, (
                start_pos[1] * grid.cell_size,
                start_pos[0] * grid.cell_size,
                grid.cell_size,
                grid.cell_size
            ))

        if end_pos:
            pygame.draw.rect(window, RED, (
                end_pos[1] * grid.cell_size,
                end_pos[0] * grid.cell_size,
                grid.cell_size,
                grid.cell_size
            ))

        pygame.display.update()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
