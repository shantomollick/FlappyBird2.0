import pygame
import os , sys
from game import Game

pygame.init()


# Global Variables
SCREENWIDTH = 360
SCREENHEIGHT = 640
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("FLAPPY BIRD 2.0")
PLAYER = 'game_sprites/bird02.png'
BACKGROUND = 'game_sprites/bg.png'
PIPE = 'game_sprites/pillar0.png'

FPS = 40
FPSCLOCK = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            Game.intro(SCREEN)
            Game.welcome(SCREEN, SCREENWIDTH, SCREENHEIGHT)
            Game.maingame(SCREEN, SCREENWIDTH, SCREENHEIGHT)
    pygame.display.update()
    FPSCLOCK.tick(FPS)