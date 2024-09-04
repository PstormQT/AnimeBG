import pygame 
import sys
sys.path.insert(0,"src\pygame\assets\classesAndUtil")
import pygame.assets.classesAndUtil.gameUtil as gameUtil
import pygame.assets.classesAndUtil.gameUtil as Button


BGColor = (28,92,76)
mainImage = "src\pygame\assets\image\AnswerButton.png"

completed_round = set()

def mainGame():
    pygame.init()
    mainWindow = pygame.display.set_mode((1000,800),pygame.RESIZABLE)
    mainWindow.fill(BGColor)
    
    #opening the json data
    
    roundCounter = 1
    
    runCheck = True
    while runCheck:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runCheck = False
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runCheck = False
                return -1

        choosenID = gameUtil.random()
        Answer1 = Button(990,540,"testing","#000000",mainWindow,mainImage,1)
        if Answer1 == True:
            print("Yatta")
        
        


if __name__ == "__main__":
    mainGame()