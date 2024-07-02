import numpy as np
import pygame
from pygame.locals import *

SCREEN_SIZE = 600

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption('BFS')

    def run(self) -> None:
        while True:
            if pygame.event.get(QUIT):
                break
            self.screen.fill('#222222')

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    Game().run()