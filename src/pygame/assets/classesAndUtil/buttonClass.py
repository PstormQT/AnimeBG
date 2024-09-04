import pygame 

class Button():
    def __init__(self,x: int,y: int,text: int, color:str, display: pygame.display, img: str) -> None:
        """
        Creating a button class and checking if clicked

        Args:
            x (int): top left of x
            y (int): top left of y
            text (int): Text on top if needed
            color (str): Color
            display (pygame.display): Pygame display to be drawned on
            img (str): the img being draw
        """
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.display = display
        self.clicked = False
        if img != None:
            width = img.get_width()
            height = img.get_height()
            self.img = pygame.transform.scale(img, (int(width), int(height)))
            
        
        
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        
        self.display.blit(self.img,self.x, self.y)
        
        return action