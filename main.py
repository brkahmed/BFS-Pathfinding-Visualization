import numpy as np
from collections import deque
import pygame
from pygame.locals import *

CELLS = 10
CELL_SIZE = 70
SCREEN_SIZE = CELLS * CELL_SIZE

EMPTY = 0
TARGET = 1
START = 2
PATH = 3
OBSTACLE = 4
TARGET_COLOR = 'red'
START_COLOR = 'blue'
PATH_COLOR = 'green'
OBSTACLE_COLOR = 'brown'
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption('BFS')
        self.map = np.zeros((CELLS, CELLS), int)
        self.start = Cell(START, START_COLOR, 0, 0, self.map)
        self.target = Cell(TARGET, TARGET_COLOR, 9, 9, self.map)
        self.map[5, 0:8] = [4] * 8

        # testing
        self.map[0:8, 1] = [OBSTACLE] * 8


    def run(self) -> None:
        while True:
            if pygame.event.get(QUIT):
                break
            self.screen.fill('#222222')
            self.draw_map()
            self.get_short_path()
            print(self.map)
            pygame.time.delay(1000)

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
                elif cell == PATH:
                    color = PATH_COLOR
                else:
                    color = OBSTACLE_COLOR
                pygame.draw.rect(self.screen,
                                 color,
                                 pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                
        for i in range(CELL_SIZE, SCREEN_SIZE, CELL_SIZE): # Start from CELL SIZE to hide the two lines in top and left
            # Draw horizantal lines
            pygame.draw.line(self.screen, 'white', (0, i), (SCREEN_SIZE, i), 2)
            #  Draw vertical lines
            pygame.draw.line(self.screen, 'white', (i, 0), (i, SCREEN_SIZE), 2)

    def get_short_path(self):
        # BFS algorithm
        to_search: deque[tuple] = deque()
        searched: set[Cell] = set()
        short_path: list[Cell] = []
        to_search.append((self.start, []))
        while to_search:
            cell, path = to_search.popleft()
            if cell in searched:
                continue
            if cell == self.target:
                short_path = path
                break
            to_search.extend((n, path + [n]) for n in self.get_neighboors(cell))
            searched.add(cell)

        for cell in short_path:
            cell.add_to_map(self.map)

    def get_neighboors(self, cell: 'Cell') -> list['Cell']:
        neighboors: list[Cell] = []
        if cell.y > 0 and self.map[cell.y - 1, cell.x] < START: # Top
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x, cell.y - 1))
        if cell.y + 1 < CELLS and self.map[cell.y + 1, cell.x] < START: # Bottm
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x, cell.y + 1))
        if cell.x > 0 and self.map[cell.y, cell.x - 1] < START: # Left
            neighboors.append(Cell(PATH, PATH_COLOR, cell.x - 1, cell.y))
        if cell.x + 1 < CELLS and self.map[cell.y, cell.x + 1] < START: # Right
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
    
    def __hash__(self) -> int:
        '''For checking with set
        this will return the hash of
        it courdinates tuple'''
        return hash((self.x, self.y))
    
    def add_to_map(self, map: np.ndarray, force: bool = False) -> None:
        if force or map[self.x, self.y] == EMPTY:
            map[self.x, self.y] = self.value

if __name__ == '__main__':
    Game().run()