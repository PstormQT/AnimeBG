import random
import time as t
import cv2
IMAGEDISPLAY = 3000

def openfile():
    directory = []
    name = []
    with open("database.txt") as file:
        for line in file:
            if line == "\n":
                pass
            else:
                line = line.split(" ")
                directory = [line[0]] + directory
                name = [line[1]] + name
    return directory, name

def main():
    print("Welcome to anime background guessing game")
    print("Please choose your difficulty:")
    print("Enter '1' for easy, 100x100% of the original image")
    print("Enter '2' for normal, 50x50% of the original image")
    print("Enter '3' for hard, 25x25% of the original image")

    difficulty = int(input("Please enter your level: "))
    start(difficulty)

def guess(name,pullname):
    print("Here are your option")
    position = random.randint(1,5)
    
    pullname = str(pullname)
    pullname = pullname.replace("_"," ")
    for x in range(1,6):
        if x != position:
            randomname = str(name[random.randint(0,len(name))])
            randomname = randomname.replace("_"," ")
            print("Enter '"+str(x)+"' for: " + str(randomname))
        else: 
            print(("Enter '"+str(x)+"' for: " + str(pullname)))
    answer = int(input("Please type your answer here: "))
    if answer == position:
        print("Yayyy you are right")
    else:
        print("You are wrong :(. Go home and watch more anime")

    
def start(dif):
    direct, name = openfile()
    length = len(direct)
    choosen = random.randint(0,length-1)
    if dif == 1:
        img = cv2.imread(direct[choosen-1])
        cv2.imshow("image",img)
        pullname = name[choosen-1]
        cv2.waitKey(IMAGEDISPLAY)
        cv2.destroyAllWindows()
        guess(name,pullname)
    elif dif == 2:
        img = cv2.imread(direct[choosen-1])
        height, width, channel = img.shape
        height = int(height)
        width = int(width)
        rheight = random.randint(0,height//2)
        rwidth = random.randint(0,width//2)
        croppedimage = img[rheight:(rheight+height//2), rwidth:(rwidth+height//2)]
        cv2.imshow("image", croppedimage)
        pullname = name[choosen-1]
        cv2.waitKey(IMAGEDISPLAY)
        cv2.destroyAllWindows()
        guess(name,pullname)
    elif dif == 3:
        img = cv2.imread(direct[choosen-1])
        height, width, channel = img.shape
        height = int(height)
        width = int(width)
        rheight = random.randint(0,height//4)
        rwidth = random.randint(0,width//4)
        croppedimage = img[rheight:(rheight+height//4), rwidth:(rwidth+height//4)]
        cv2.imshow("image", croppedimage)
        pullname = name[choosen-1]
        cv2.waitKey(IMAGEDISPLAY)
        cv2.destroyAllWindows()
        guess(name,pullname)
    else:
        print("data input is invalid so you will play the hardest dif :)")
        start(3)

if __name__ == '__main__':
    main()

 