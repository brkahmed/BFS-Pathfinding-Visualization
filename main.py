import numpy as np
import pygame
from pygame.locals import *

CELLS = 60
CELL_SIZE = 10
SCREEN_SIZE = CELLS * CELL_SIZE

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
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == 0:
                    color = 'black'
                pygame.draw.rect(self.screen,
                                 color,
                                 pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))

if __name__ == '__main__':
    Game().run()