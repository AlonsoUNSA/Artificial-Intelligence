import csv
import pygame
from settings import BLACK, WHITE

class Grid:
    def __init__(self, filename):
        self.grid = self.load_from_csv(filename)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.cell_size = 20

        # Matriz para guardar colores actuales de cada celda
        self.cell_colors = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def load_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            grid = []
            for row in reader:
                grid.append([int(cell) for cell in row])
        return grid

    def draw(self, window):
        for r in range(self.rows):
            for c in range(self.cols):
                # Color base: blanco para espacio libre, negro para obstáculo
                color = WHITE
                if self.grid[r][c] == 1:
                    color = BLACK
                
                # Si la celda tiene color asignado (del algoritmo), usarlo
                if self.cell_colors[r][c] is not None:
                    color = self.cell_colors[r][c]

                pygame.draw.rect(window, color, (
                    c * self.cell_size,
                    r * self.cell_size,
                    self.cell_size,
                    self.cell_size
                ))

    def color_cell(self, row, col, color):
        self.cell_colors[row][col] = color

