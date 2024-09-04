import pygame, gameUtil

BGColor = (28,92,76)

completed_round = set()

def mainGame():
    pygame.init()
    mainWindow = pygame.display.set_mode((1000,800),pygame.RESIZABLE)
    mainWindow.fill(BGColor)
    
    
    roundCounter = 1
    
    runCheck = True
    while runCheck:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runCheck = False
        
        
        
        
        
def singleRound(roundCounter, mainWindow):
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
        
        
        


if __name__ == "__main__":
    mainGame()