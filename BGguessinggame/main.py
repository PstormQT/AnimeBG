import random
import time as t
import cv2
from dataclasses import dataclass
IMAGEDISPLAY = 5000

def main():
    print("Welcome to anime guessing game")
    print("Please choose your difficulty:")
    print("Enter '1' for easy, 100x100% of the original image")
    print("Enter '2' for normal, 50x50% of the original image")
    print("Enter '3' for hard, 33x33% of the original image")
    difficulty = int(input("Please enter your level: "))
    anime = ImageGuess("animedatabase.txt",difficulty)
    anime.start()
    
        
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
    
    def start(self):
        if self.dif == 1:
            bgdata = ImageGuess.openfile(self)
            length = len(bgdata)
            choosen = random.randint(0,length-1)
            directory = bgdata[choosen-1].location
            img = cv2.imread(directory)
            cv2.imshow("Background",img)
            cv2.waitKey(IMAGEDISPLAY)
            cv2.destroyAllWindows()
            ImageGuess.answer(self,bgdata,bgdata[choosen-1].name)
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
            ImageGuess.answer(self,bgdata,bgdata[choosen-1].name)
            
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
    
if __name__ == '__main__':
    main()
