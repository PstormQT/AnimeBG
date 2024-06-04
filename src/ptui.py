import model, cv2, numpy as np, urllib.request

BASE_URL = "https://uploads.mangadex.org/covers/"

def run():
    print("Welcome to anime background game")
    while True:
        dif = input("Please input your difficulty: ")
        time = input("Please input your time limit in seconds (Max 120 seconds, type -1 for no timer)")
        top = input("Please enter the top manga ranking (Input 0 for default value, 20):")
        runTime = input("Please enter amount of run time (Default value of 10)")
        print()
        
        game = model.Level(top,dif,time,runTime)      
        game.checkFetching()
        print("You had pick the guess the manga cover with stat of: ")
        print("Top " + top + " Manga")
        if time == -1:
            print("With no time limit")
        else: 
            print("With time limit of " +  time + " seconds")
        print("With the difficulty level of " + dif)
        print("With " + runTime + " round(s) of the game")
        print()
        print("Type \"quit\" as an answer to quit at any time")
        
        for roundCounter in range(runTime):
            game.generateNewLevel()
            levelData = game.getFetchData()
            currentLevel = game.getLevel(roundCounter)
            print("Here is your manga cover")
            
            answerLocation = currentLevel[4]
            
            url = BASE_URL + levelData.get
            