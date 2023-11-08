import pygame
import backgroundlogic

pygame.init()


class GameWindow:
    def run(self,width,height):
        screen = pygame.display.set_mode((width,height))

        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 

    pygame.quit()
    
    def imagepull(self):
        logicinit = backgroundlogic.ImageData("animedatabase.txt",str(-1))
        animedata = 


anime = GameWindow()
anime.run(1980,1080)