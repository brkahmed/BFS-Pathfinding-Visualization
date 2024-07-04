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
OBSTACLE = 3
PATH = 4

TARGET_COLOR = 'red'
START_COLOR = 'blue'
PATH_COLOR = 'green'
OBSTACLE_COLOR = 'gray'
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption('BFS')
        self.map: np.ndarray = np.loadtxt('map.csv', 'uint8', delimiter=',')

        indices: tuple = np.where(self.map == START)
        self.start: Cell = Cell(START, START_COLOR, indices[1][0], indices[0][0], self.map)
        indices: tuple = np.where(self.map == TARGET)
        self.target: Cell = Cell(TARGET, TARGET_COLOR, indices[1][0], indices[0][0], self.map)

    def run(self) -> None:
        while True:
            if pygame.event.get(QUIT):
                break

            path = self.find_short_path()
            self.draw_map()
            self.draw_path(path)
            pygame.display.flip()

            pygame.time.delay(3000)

        pygame.quit()

    def draw_map(self) -> None:
        self.screen.fill('#222222')
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

    def draw_path(self, path: list['Cell']) -> None:
        for cell in path:
            pygame.draw.rect(
                self.screen,
                cell.color,
                pygame.Rect(cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def find_short_path(self) -> list['Cell']:
        # BFS algorithm
        to_search: deque[tuple] = deque()
        searched: set[Cell] = set()
        short_path: list[Cell] = []

        to_search.append((self.start, []))

        while to_search:
            cell, path = to_search.popleft()
            
            # Draw the current path
            self.draw_map()
            self.draw_path(path)
            pygame.display.flip()
            pygame.time.delay(200)

            if cell in searched:
                continue
            if cell == self.target:
                short_path = path[:-1] # to not include the target
                break
            to_search.extend((n, path + [n]) for n in self.find_neighboors(cell))
            searched.add(cell)

        return short_path

    def find_neighboors(self, cell: 'Cell') -> list['Cell']:
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
    def __init__(self, value: int, color: str, x: int, y: int, map: np.ndarray | None = None) -> None:
        self.value: int = value
        self.color: str = color
        self.x: int = x 
        self.y: int = y
        if map is not None:
            self.add_to_map(map, force=True)

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
        if force or map[self.y, self.x] == EMPTY:
            map[self.y, self.x] = self.value

if __name__ == '__main__':
    Game().run()