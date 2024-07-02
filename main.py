import numpy as np
import pygame
from pygame.locals import *

CELLS = 10
CELL_SIZE = 70
SCREEN_SIZE = CELLS * CELL_SIZE

START = 1
START_COLOR = 'blue'
TARGET = 2
TARGET_COLOR = 'red'
PATH = 3
PATH_COLOR = 'green'

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption('BFS')
        self.map = np.zeros((CELLS, CELLS), 'uint8')

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

if __name__ == '__main__':
    Game().run()