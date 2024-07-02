import numpy as np
import pygame
from pygame.locals import *

CELLS = 10
CELL_SIZE = 70
SCREEN_SIZE = CELLS * CELL_SIZE

EMPTY = 0
PATH = 1
TARGET = 2
START = 3
TARGET_COLOR = 'red'
START_COLOR = 'blue'
PATH_COLOR = 'green'

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption('BFS')
        self.map = np.zeros((CELLS, CELLS), 'uint8')
        self.start = Cell(START, START_COLOR, 0, 0, self.map)

    def run(self) -> None:
        while True:
            if pygame.event.get(QUIT):
                break
            self.screen.fill('#222222')
            self.draw_map()

            pygame.display.flip()

        pygame.quit()

    def draw_map(self) -> None:
        # Draw cells in the map dependig on their value
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == EMPTY: # if cell is zero keep the background color
                    continue
                if cell == START:
                    color = START_COLOR
                elif cell == TARGET:
                    color = TARGET_COLOR
                else:
                    color = PATH_COLOR
                pygame.draw.rect(self.screen,
                                 color,
                                 pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
        for i in range(CELL_SIZE, SCREEN_SIZE, CELL_SIZE): # Start from CELL SIZE to hide the two lines in top and left
            # Draw horizantal lines
            pygame.draw.line(self.screen, 'white', (0, i), (SCREEN_SIZE, i), 2)
            #  Draw vertical lines
            pygame.draw.line(self.screen, 'white', (i, 0), (i, SCREEN_SIZE), 2)

    def get_neighboors(self, cell: 'Cell') -> list['Cell']:
        neighboors: list[Cell] = []
        if cell.y - 1 > 0 and self.map[cell.y - 1, cell.x] < START:
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x, cell.y - 1))
        if cell.y + 1 < CELLS and self.map[cell.y + 1, cell.x] < START:
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x, cell.y + 1))
        if cell.x - 1 > 0 and self.map[cell.y, cell.x - 1] < START:
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x - 1, cell.y))
        if cell.x + 1 < CELLS and self.map[cell.y, cell.x + 1] < START:
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x + 1, cell.y))
        return neighboors

class Cell:
    def __init__(self, value: int, color: str, x: int, y: int, map: np.ndarray = None) -> None:
        self.value = value
        self.color = color
        self.x = x 
        self.y = y
        if map is not None:
            self.add_to_map(map)

    def __repr__(self) -> str:
        return f'Cell(value({self.value}), courdinate({self.x}, {self.y}))'

    def __eq__(self, other: 'Cell') -> bool:
        return self.x == other.x and self.y == other.y
    
    def add_to_map(self, map: np.ndarray) -> None:
        map[self.x, self.y] = self.value

if __name__ == '__main__':
    Game().run()