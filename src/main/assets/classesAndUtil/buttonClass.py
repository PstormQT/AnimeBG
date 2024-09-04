import pygame 

class Button():
    def __init__(self,x: int,y: int,text: int, color:str, display: pygame.display, img: str, scale: int) -> None:
        """
        Creating a button class and checking if clicked

        Args:
            x (int): top left of x
            y (int): top left of y
            scale(float): scaling of image if needed
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
        self.text_rect = None
        if img != None:
            self.width = img.get_width()
            self.height = img.get_height()
            self.img = pygame.transform.scale(img, (int(self.width)*scale, int(self.height)*scale))           
    
        
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
        self.write()
        self.display.blit(self.text,self.text_rect)
        return action
    
    
    def write(self):
        font = pygame.font.SysFont("Comic Sans MS", 14)
        self.text = font.render(self.text, 1, pygame.Color(self.color))
        self.text_rect = self.text.get_rect(center=((self.x+self.width//2),(self.y+self.height//2) ))
        