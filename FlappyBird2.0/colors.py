class Colors:
   
    White = (255, 255, 255)
    Green = (0, 110, 0)
    Light_green = (0, 225, 0)
    Red = (255, 0, 0)
    Light_Green = (0, 180, 0)
        


    # def maingame(self,screen, screen_width, screen_height, fps):
    #     score = 0
    #     playerx = int(screen_width/5)
    #     playery = int(screen_width/2)
    #     basex = 0
    #     GROUNDY = 640 * 0.804
    #     FPS = fps
    #     FPSClock = pygame.time.Clock()
    


    #     NewPipe1 = Functions.get_random_pipe(screen_width, screen_height)
    #     NewPipe2 = Functions.get_random_pipe(screen_width, screen_height)


    #     UpperPipes = [
    #         {'x' : screen_width + 200, 'y' : NewPipe1[0]['y']},
    #         {'x' : screen_width + 200 + (screen_width/2), 'y' : NewPipe2[0]['y']}
    #     ]

    #     LowerPipes = [
    #         {'x' : screen_width + 200, 'y' : NewPipe1[1]['y']},
    #         {'x' : screen_width + 200 + (screen_width/2), 'y' : NewPipe2[1]['y']}
    #     ]


    #     PipeVelX = -4
    #     PlayerMaxVelY = 13
    #     # PlayerMinVelY = -8
    #     PlayerVelY = -5
    #     PlayerAccY = 1
    #     PlayerFlapAcc = -9
    #     PlayerFlapped = False

    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
    #                 pygame.quit()
    #                 quit()
    #             if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
    #                 if playery > 0:
    #                     PlayerVelY = PlayerFlapAcc
    #                     PlayerFlapped = True
    #                     Tools.GameSounds['wing'].play()

    #         CrashTest = Functions.is_collide()
    #         if CrashTest:
    #             return

    #         PlayerMidPos = playerx + Tools.GameSprites['player'].convert_alpha().get_width()/2
    #         for pipe in UpperPipes:
    #             PipeMidPos = pipe['x'] + Tools.GameSprites['pipe'][0].get_width()/2
    #             if PipeMidPos <= PlayerMidPos < PipeMidPos + 7:
    #                 score+=1
    #                 Tools.GameSounds['point'].play()

    #             # if PlayerVelY >= PlayerMinVelY and not PlayerFlapped:
    #             if PlayerVelY < PlayerMaxVelY and not PlayerFlapped:
    #                 PlayerVelY += PlayerAccY

               
                    

    #             if PlayerFlapped:
    #                 PlayerFlapped = False

    #             PlayerHeight = Tools.GameSprites['player'].convert_alpha().get_height()
    #             playery = playery + min(PlayerVelY, GROUNDY - playery - PlayerHeight)


    #             for upperpipe , lowerpipe in zip(UpperPipes, LowerPipes):
    #                 upperpipe['x'] += PipeVelX
    #                 lowerpipe['x'] += PipeVelX 

    #             if 0 < UpperPipes[0]['x'] < 7:
    #                 NewPipe = Functions.get_random_pipe(screen_width, screen_height)
    #                 UpperPipes.append(NewPipe[0])
    #                 LowerPipes.append(NewPipe[1])

    #             if UpperPipes[0]['x'] < - Tools.GameSprites['pipe'][0].get_width():
    #                 UpperPipes.pop(0)
    #                 LowerPipes.pop(0)

    #             screen.blit(Tools.GameSprites['background'].convert_alpha(), (0, 0))
    #             for upperpipe , lowerpipe in zip(UpperPipes, LowerPipes):
    #                 screen.blit(Tools.GameSprites['pipe'][0], (upperpipe['x'], upperpipe['y']))
    #                 screen.blit(Tools.GameSprites['pipe'][1], (lowerpipe['x'], lowerpipe['y']))

    #             screen.blit(Tools.GameSprites['base'].convert_alpha(), (basex, GROUNDY))
    #             screen.blit(Tools.GameSprites['player'].convert_alpha(), (playerx, playery))

    #         pygame.display.update()
    #         FPSClock.tick(FPS)