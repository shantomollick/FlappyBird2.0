import pygame
pygame.init()
import sys

from functions import Functions
from sprites import Tools

class Game:
    GROUNDY = 640 * 0.804
    @classmethod
    def intro(self, screen):
        intro = False
        background = Tools.GameSprites['background'].convert_alpha()
        while intro==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = True
                    pygame.quit()
                    quit()
            screen.blit(background, (0, 0))
            Play_button = Functions.button(screen, 50, 300, "Play")
            Quit_button = Functions.button(screen, 210, 300, "Quit")
            if Play_button == True:
                return
            if Quit_button == True:
                intro = True
                pygame.quit()
                quit()
                
            pygame.display.update()
    
    @classmethod
    def welcome(self,screen, screen_width, screen_height):
        playerx = int(screen_width/5)
        playery = int((screen_height - Tools.GameSprites['player'].convert_alpha().get_height())/2)
        messagex = int((screen_width - Tools.GameSprites['message'].convert_alpha().get_width())/2)
        messagey = int(screen_height*0.0005)
        basex = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
                    pygame.quit() 
                    sys.exit()  
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    return 

                else:
                    screen.blit(Tools.GameSprites['background'].convert_alpha(), (0, 0))
                    screen.blit(Tools.GameSprites['player'].convert_alpha(), (playerx, playery))
                    screen.blit(Tools.GameSprites['message'].convert_alpha(), (messagex, messagey))
                    screen.blit(Tools.GameSprites['base'].convert_alpha(), (basex, self.GROUNDY))
                    Back_button = Functions.button(screen, 10, 600, "Back ")
                    if Back_button == True:
                        self.intro(screen)

                pygame.display.update()

    @classmethod
    def maingame(self,screen, screen_width, screen_height, FPS=40):
        score = 0
        playerx = int(screen_width/5)
        playery = int(screen_width/2)
        basex = 0
        GROUNDY = 640 * 0.804
        FPSClock = pygame.time.Clock()
    


        NewPipe1 = Functions.get_random_pipe(screen_width, screen_height)
        NewPipe2 = Functions.get_random_pipe(screen_width, screen_height)


        UpperPipes = [
            {'x' : screen_width + 200, 'y' : NewPipe1[0]['y']},
            {'x' : screen_width + 200 + (screen_width/2), 'y' : NewPipe2[0]['y']}
        ]

        LowerPipes = [
            {'x' : screen_width + 200, 'y' : NewPipe1[1]['y']},
            {'x' : screen_width + 200 + (screen_width/2), 'y' : NewPipe2[1]['y']}
        ]
       


        PlayerVelY = -5
        PlayerFlappAccY = -9
        PlayerFlapped = False
        PipeVelX = -4
        PlayerMaxVelY = 13
        PlayerAccY = 1

        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    if playery > 0:
                        PlayerVelY = PlayerFlappAccY
                        PlayerFlapped = True
                        Tools.GameSounds['wing'].play()
                

            CrashTest = Functions.is_collide()
            if CrashTest:
                return
            
            PlayerMidPos = playerx + Tools.GameSprites['player'].get_width()
            for pipe in UpperPipes:
                PipeMidPos = pipe['x'] + Tools.GameSprites['pipe'][0].get_width()/2
                if PipeMidPos < PlayerMidPos < PipeMidPos + 15:
                    score += 1
                    Tools.GameSounds['point'].play()

                if PlayerVelY < PlayerMaxVelY and not PlayerFlapped:
                    PlayerVelY += PlayerAccY

                if PlayerFlapped:
                    PlayerFlapped = False

                PlayerHeight = Tools.GameSprites['player'].get_height()
                playery = playery + min(PlayerVelY, GROUNDY - PlayerHeight - playery)

                for UpperPipe , LowerPipe in zip(UpperPipes, LowerPipes):
                    UpperPipe['x'] += PipeVelX
                    LowerPipe['x'] += PipeVelX

                if 0 < UpperPipes[0]['x'] < 7:
                    NewPipe = Functions.get_random_pipe(screen_width, screen_height)
                    UpperPipes.append(NewPipe[0])
                    LowerPipes.append(NewPipe[1])

                if UpperPipes[0]['x'] < -Tools.GameSprites['pipe'][0].get_width():
                    UpperPipes.pop(0)
                    LowerPipes.pop(0)

                screen.blit(Tools.GameSprites['background'], (0, 0))
                for UpperPipe , LowerPipe in zip(UpperPipes, LowerPipes):
                    screen.blit(Tools.GameSprites['pipe'][0], (UpperPipe['x'], UpperPipe['y'])),
                    screen.blit(Tools.GameSprites['pipe'][1], (LowerPipe['x'], LowerPipe['y']))

                screen.blit(Tools.GameSprites['player'], (playerx, playery))
                screen.blit(Tools.GameSprites['base'], (basex, GROUNDY))
                # Functions.Score_surface(screen, score, screen_width, screen_height)
                MyDigits = (int(x) for x in list(str(score)))
                width = 0
                for Digits in MyDigits:
                    width += Tools.GameSprites['numbers'][Digits].get_width()
                Xoffset = (screen_width - width)/2
                for digit in MyDigits:
                        screen.blit(Tools.GameSprites['numbers'][digit], (Xoffset, screen_height*0.12))
                        Xoffset += Tools.GameSprites['numbers'][digit].get_width()

                pygame.display.update()
                FPSClock.tick(FPS)