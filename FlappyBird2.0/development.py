import pygame
import sys
import random
from pygame.locals import *
import time

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

# Color
White = (255,255,255)
Green = (0,255,0)
light_green = (0,110,0)
Red = (255,0,0)

# first welcome page
def message(size, mess, x_pos, y_pos,color=White):
    font = pygame.font.SysFont(None,size)
    render = font.render(mess,True,color)
    SCREEN.blit(render, [x_pos,y_pos])


def button(x_button,y_button,mess_b):
    pygame.draw.rect(SCREEN, Green, [x_button,y_button,100,30])
    message(40, mess_b, x_button+20, y_button+2.5)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(SCREEN, light_green, [x_button,y_button,100,30])
        message(40, mess_b, x_button + 20, y_button)
        if click==(1,0,0) and mess_b=="Play":
            welcomeScreen()
        elif click==(1,0,0) and mess_b=="Quit":
            pygame.quit()
            quit()


def intro():
    intro = False
    background = pygame.image.load("gamesprites/bg.png")
    while intro==False:
        SCREEN.blit(background, (0, 0))
        button(50,300,"Play")
        button(210,300,"Quit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
                pygame.quit()
                quit()
        pygame.display.update()


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
                mainGame()
            
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0, 0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/4
    y2 = offset + 10 + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - SCREENHEIGHT/3))
    pipeX = SCREENWIDTH + 20
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 61 or playery<0:
        GAME_SOUNDS['hit'].play()
        message(30,"Crashed!",130,300,Red)
        pygame.display.update()
        time.sleep(2)
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playery < pipeHeight + pipe['y'] and abs(playerx - (pipe['x']) - 10) < GAME_SPRITES['pipe'][0].get_width() - 15):
           GAME_SOUNDS['hit'].play()
           message(30,"Crashed!",130,300,Red)
           pygame.display.update()
           time.sleep(2)
           return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x'] - 10) < GAME_SPRITES['pipe'][0].get_width() - 15:
            # message(20,"Crashed",SCREENWIDTH/2,SCREENHEIGHT/2)
            GAME_SOUNDS['hit'].play()
            message(30,"Crashed!",130,300,Red)
            pygame.display.update()
            time.sleep(2)
            return True
    return False





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
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y': newPipe2[0]['y']}
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
    game_paused = False  

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

            # if event.type == pygame.K_ESCAPE:    
            #     game_paused = not game_paused


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return
        
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 7:
                score += 1
                # print(f"Your score is {score}")
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


            if 0 < upperPipes[0]['x'] < 7:
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
        intro()
