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
        self.start = Cell(START, START_COLOR, 5, 5)

    def run(self) -> None:
        while True:
            if pygame.event.get(QUIT):
                break
            self.screen.fill('#222222')
            self.draw_map()
            print(self.get_neighboors(self.start))
            pygame.display.flip()

        pygame.quit()

    def draw_map(self) -> None:
        # Draw cells in the map dependig on their value
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == 0: # if cell is zero keep the background color
                    continue
                if cell == START:
                    color = START_COLOR
                elif cell == TARGET:
                    color = TARGET_COLOR
                elif cell == PATH:
                    color = PATH_COLOR
                pygame.draw.rect(self.screen,
                                 color,
                                 pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
        for i in range(CELL_SIZE, SCREEN_SIZE, CELL_SIZE): # Start from CELL SIZE to hide the two lines in top and left
            # Draw horizantal lines
            pygame.draw.line(self.screen, 'white', (0, i), (SCREEN_SIZE, i), 2)
            #  Draw vertical lines
            pygame.draw.line(self.screen, 'white', (i, 0), (i, SCREEN_SIZE), 2)

    def get_neighboors(self, cell: 'Cell') -> list:
        neighboors: list[Cell] = []
        for i in range(max(0, cell.x -1), min(cell.x + 2, self.map.shape[1]), 2):
            if self.map[cell.y, i] < START:
                neighboors.append(Cell(PATH, PATH_COLOR, i, cell.y))

        for i in range(max(0, cell.y -1), min(cell.y + 2, self.map.shape[0]), 2):
            if self.map[i, cell.x] < START:
                neighboors.append(Cell(PATH, PATH_COLOR, cell.x, i))
        return neighboors

class Cell:
    def __init__(self, value: int, color: str, x: int, y: int) -> None:
        self.value = value
        self.color = color
        self.x = x 
        self.y = y

    def __repr__(self) -> str:
        return f'Cell(value({self.value}), courdinate({self.x}, {self.y}))'

    def __eq__(self, other: 'Cell') -> bool:
        return self.x == other.x and self.y == other.y
    
    def add_to_map(self, map: np.ndarray) -> None:
        map[self.y, self.x] = self.value

if __name__ == '__main__':
    Game().run()