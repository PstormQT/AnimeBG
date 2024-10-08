import pygame 
import assets.classesAndUtil.gameUtil as gameUtil
import assets.classesAndUtil.buttonClass as ButtonTem
import assets.classesAndUtil.fetching as fetching


BGColor = (28,92,76)
mainImage = "assets\\image\\AnswerButton.jpg"

completed_round = set()

def mainGame():
    pygame.init()
    mainWindow = pygame.display.set_mode((1000,800),pygame.RESIZABLE)
    mainWindow.fill(BGColor)
    pygame.display.update()
    #opening the json data
    
    roundCounter = 1
    
    runCheck = True
    singleRound(1,mainWindow)
        
        
        

        
        
def singleRound(roundCounter: int, mainWindow: pygame.display):
    """
    The implementation for a single round

    Args:
        roundCounter (int): What round is it
        mainWindow (pygame.display): The main game window

    Returns:
        int : return the round that was use, ONLY return -1 if quit
    """
    w, h = pygame.display.get_surface().get_size()
    
    
    
    runCheck = True
    while runCheck:
        
        #Refill BG
        mainWindow.fill(BGColor)
        
        
        main
        #Creating button
        Answer1 = ButtonTem.Button(500,500,"testing","#ffffff",mainWindow,mainImage,1)
        if Answer1.draw() == True:
            print("Yatta")
        
        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runCheck = False
                
        
        #updating the window
        pygame.display.update()

        # choosenID = gameUtil.pickRandomOmit(0,1,(1,2))
        
        
        


if __name__ == "__main__":
    mainGame()