import pygame
import random
import cv2
import time
from dataclasses import dataclass
IMAGEDISPLAY = 5000
SCREENWIDTH = 1600
SCREENHEIGHT = 800
IMAGEHEIGHT = 400
IMAGEWIDTH = 300

def main():
    print("Welcome to the guessing game")
    print("Please choose your genre:")
    print("Enter 'A' for Terminal Game")
    print("Enter 'B' for Launcher Game")
    genre = str(input("Please choose your window type: "))
    if genre == "A":
        genrepass = UserStart()
        genrepass.animeprompt()
    if genre == "B":
        genrepass = UserStart()
        genrepass.monitorinit()
        
@dataclass
class ImageData:
    name: str
    location: str
        
class ImageGuess:
    def __init__(self,database,dif):
        self.database = database
        self.dif = dif
        
    def openfile(self):
        imageinfo = []
        with open(str(self.database)) as file:
            for line in file:
                if line == "\n":
                    pass
                else:
                    line = line.split(" ")
                    location = str(line[0])
                    name = str(line[1])
                    imageinfo.append(ImageData(name,location))
        return imageinfo
    
    def imageshow(self):
        if self.dif == 1:
            bgdata = ImageGuess.openfile(self)
            length = len(bgdata)
            choosen = random.randint(0,length-1)
            directory = bgdata[choosen-1].location
            img = cv2.imread(directory)
            cv2.imshow("Background",img)
            cv2.waitKey(IMAGEDISPLAY)
            cv2.destroyAllWindows()
            return self,bgdata,bgdata[choosen-1].name
        else:
            bgdata = ImageGuess.openfile(self)
            length = len(bgdata)
            choosen = random.randint(0,length-1)
            directory = bgdata[choosen-1].location
            img = cv2.imread(directory)
            height, width, channel = img.shape
            height = int(height)
            width = int(width)
            rheight = random.randint(0,height//self.dif)
            rwidth = random.randint(0,width//self.dif)
            croppedimage = img[rheight:(rheight+height//self.dif),
                            rwidth:(rwidth+height//self.dif)]
            cv2.imshow("Background",croppedimage)
            cv2.waitKey(IMAGEDISPLAY)
            cv2.destroyAllWindows()
            return self,bgdata,bgdata[choosen-1].name
            
    def answer(self,database,correctanime):
        print("Here are your option")
        position = random.randint(1,5)
        
        correctanime = str(correctanime)
        correctanime = correctanime.replace("_"," ")
        for x in range(1,6):
            if x != position:
                randomname = str(database[random.randint(0,len(database))].name)
                randomname = randomname.replace("_"," ")
                print("Enter '"+str(x)+"' for: " + str(randomname))
            else: 
                print(("Enter '"+str(x)+"' for: " + str(correctanime)))
        answer = int(input("Please type your answer here: "))
        if answer == position:
            print("Yayyy you are right")
        else:
            print("You are wrong :( Go home and watch more anime")
            print("The answer is: " + str(correctanime))   


class GameInit:
    score = 0
    
    def __init__(self,bgdata):
        self.bgdata = bgdata
    
    def pullingbg(self):
        # background = pygame.
        # return background
        pass
    
    def homepage(self):
        screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        color = ("#8ea1f5")
        pygame.draw.rect(screen,color,pygame.Rect(SCREENWIDTH/4,SCREENHEIGHT/4,SCREENWIDTH/2,SCREENHEIGHT))
        pygame.display.flip()
        
        pygame.display.update()
        
        
    def run(self):
        screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        length = len(self.bgdata)
        choosen = random.randint(0,length-1)
        directory = self.bgdata[choosen-1].location
        img = pygame.image.load(directory).convert()
        screen.fill("#4399a1")
        screen.blit(img,(SCREENWIDTH/2 - IMAGEWIDTH/2,
                         SCREENHEIGHT/20))
        pygame.display.flip()
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
        time.sleep(2000)
        screen.fill("#000000")
        

class UserStart:
    def animeprompt(self):
        print("You choose anime guessing game")
        print("Please choose your difficulty:")
        print("Enter '1' for easy, 100x100% of the original image")
        print("Enter '2' for normal, 50x50% of the original image")
        print("Enter '3' for hard, 33x33% of the original image")
        difficulty = int(input("Please enter your level: "))
        anime = ImageGuess("animedatabase.txt",difficulty)
        self,bgdata,bgname= anime.imageshow()
        anime.answer(bgdata,bgname)
        
    def monitorinit(self):
        anime = ImageGuess("ppanimedatabase.txt",str(-1))
        bgdata = anime.openfile()
        gameopen = GameInit(bgdata)
        gameopen.run()
        
if __name__ == '__main__':
    main()
