from colors import Colors
from sprites import Tools
import pygame
import sys , random, time
pygame.init()



class Functions:
    @classmethod
    def message(self, screen, size, mess, x, y, color = Colors.White):
        font = pygame.font.SysFont(None, size)
        render = font.render(mess, True, color)
        screen.blit(render, [x,y])

    
    @classmethod
    def button(self, screen, x_button, y_button, message, width=100, height=30, color = Colors.White):
            pygame.draw.rect(screen, Colors.Light_Green, [x_button-7.5, y_button-5, 115, 40], 0, 9)
            pygame.draw.rect(screen, Colors.Light_green, [x_button, y_button, width, height], 0, 9)
            self.message(screen, int(width*height*0.014), message, x_button+(width*0.21), y_button+(height*0.066))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x_button <= mouse[0] <= x_button+width and y_button <= mouse[1] < y_button+height:
                 pygame.draw.rect(screen, Colors.Green, [x_button, y_button, width, height], 0, 9)
                 self.message(screen, int(width*height*0.013), message, x_button+(width*0.21), y_button+(height*0.066))
                 if click == (1, 0, 0) and message == message:
                      return True
                 else:
                      return False

    @classmethod
    def get_random_pipe(self, screen_width, screen_height):
         PipeHeight = Tools.GameSprites['pipe'][0].get_height()
         offset = screen_height/4
         pipex = screen_width + 20
         y2 = offset + 10 + random.randrange(0, int(screen_height - Tools.GameSprites['base'].get_height() - screen_height/3))
         y1 = PipeHeight - y2 + offset
         pipe = [
              {'x' : pipex, 'y' : -y1},
              {'x' : pipex, 'y' : y2}
         ]
         return pipe
     
    @classmethod
    def is_collide(self,screen, playerx, playery, GROUNDY, UpperPipes, LowerPipes):
        #  if playery > GROUNDY - 61 or playery < 0:
        #       Tools.GameSounds['hit'].play()
        #       self.message(screen, 30, "Crashed", 130, 300)
        #       pygame.display.update()
        #       time.sleep(2)
        #       return True
        #  for pipe in UpperPipes:
        #     PipeHeight = Tools.GameSprites['pipe'][0].get_height()
        #     if playery < 
         return False

#     @classmethod
#     def Score(self,score, pipe, PlayerMidPos):
#           PipeMidPos = pipe['x'] + Tools.GameSprites['pipe'][0].get_width()/2
#           if PipeMidPos < PlayerMidPos < 7:
#                score += 1
               
#                print(f"Your score {score}")
#                return score, Tools.GameSounds['point'].play()
    @classmethod
    def Score_surface(self, screen, score, screen_width, screen_height):
        MyDigits = (int(x) for x in list(str(score)))
        width = 0
        for Digits in MyDigits:
            width += Tools.GameSprites['numbers'][Digits].get_width()
        Xoffset = (screen_width - width)/2
        for digit in MyDigits:
                screen.blit(Tools.GameSprites['numbers'][digit], (Xoffset, screen_height*0.12))
                Xoffset += Tools.GameSprites['numbers'][digit].get_width()
                pygame.display.update()
        
              
