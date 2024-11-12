import pygame
import sys
import random
from pygame.locals import *

# Global Variables
FPS = 30
SCREENWIDTH = 360
SCREENHEIGHT = 640
SCREEN =  pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.804
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gamesprites/bird02.png'
BACKGROUND = 'gamesprites/bg.png'
PIPE = 'gamesprites/pillar0.png'
game_paused = False


def welcomeScreen():
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT * 0.0005)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0, 0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # creating two pipes 
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']},
    ]

    lowerPipes = [
            {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
            {'x': SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[1]['y']},
        ]

    pipevelX = -4
    playerMaxVelY = 13
    playerVelY = -5
    # playerMinVelY = -8
    playerAccY = 1

    playerFlappAcc = -9
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0 :
                    playerVelY = playerFlappAcc
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
            elif event.type == KEYDOWN and event.key == K_p:
                game_paused = not game_paused
                if game_paused:
                    # Display "PAUSED" message
                    paused_surface = pygame.font.Font(None, 36).render("PAUSED", True, (255, 255, 255))
                    paused_rect = paused_surface.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))
                    SCREEN.blit(paused_surface, paused_rect)
                    pygame.display.update()
        
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return
        
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 7:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

            if playerVelY < playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False
            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)


            for upperPipe , lowerpipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipevelX
                lowerpipe['x'] += pipevelX


            if 0 < upperPipes[0]['x'] < 5:
                newPipe = getRandomPipe()
                upperPipes.append(newPipe[0])
                lowerPipes.append(newPipe[1])

            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
                                              
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe ,lowerpipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerpipe['x'], lowerpipe['y']))
            
            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 61 or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x'] - 10) < GAME_SPRITES['pipe'][0].get_width() - 15):
           GAME_SOUNDS['hit'].play()
           return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x'] - 10) < GAME_SPRITES['pipe'][0].get_width() - 15:
            GAME_SOUNDS['hit'].play()
            return True
        
    return False

def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/4
    y2 = offset +10 + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - SCREENHEIGHT/3))
    pipeX = SCREENWIDTH + 20
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe


                

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('FlappyBird by Shanto')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gamesprites/00.png').convert_alpha(),
        pygame.image.load('gamesprites/01.png').convert_alpha(),
        pygame.image.load('gamesprites/02.png').convert_alpha(),
        pygame.image.load('gamesprites/03.png').convert_alpha(),
        pygame.image.load('gamesprites/04.png').convert_alpha(),
        pygame.image.load('gamesprites/05.png').convert_alpha(),
        pygame.image.load('gamesprites/06.png').convert_alpha(),
        pygame.image.load('gamesprites/07.png').convert_alpha(),
        pygame.image.load('gamesprites/08.png').convert_alpha(),
        pygame.image.load('gamesprites/09.png').convert_alpha()
)
    
    GAME_SPRITES['message'] = pygame.image.load('gamesprites/welcome1.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gamesprites/base2.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SOUNDS['die'] = pygame.mixer.Sound('gamesounds/sfx_die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gamesounds/sfx_hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gamesounds/sfx_point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gamesounds/sfx_swooshing.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gamesounds/sfx_wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    while True:
        welcomeScreen()
        mainGame()