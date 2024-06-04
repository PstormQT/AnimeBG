import json, datetime, fetching, random

class Level:
    source = "MangadexTop1000Full.json"
    def __init__(self, top : int, difficulty : int, time : int, runTime : int):
        """
        Indicate req leve

        Args:
            top (int): Level req
            difficulty (int): difficulty req
            time (int): Time Counter
            data (Dict: Dict: String): The Anime pull 
        """
        self.top = top
        self.difficulty = difficulty
        self.time = time
        self.data = None
        self.runTime = runTime
        self.levelList = []
        
    def __init__(self):
        """
        Overlaod the main class with default value
        """
        self.top = 20
        self.difficulty = 0
        self.time = -1
        self.data = None
        self.runTime = 10
        self.levelList = []
        
    
    def checkFetching(self):
        """Fetching the json file recheck if needed"""
        reading = open(self.source, "r")
        self.data = json.load(reading)
        
        current = datetime.datetime.now()
        if self.data.get("0").get("year") != current.year or self.data.get("0").get("month") != current.month:
            fetching.dumpingToFile()
            reading = open(self.source, "r")
            self.data = json.load(reading)    
            
    def getFetchData(self):
        """Fetching the json file recheck if needed"""
        reading = open(self.source, "r")
        self.data = json.load(reading)
        
        current = datetime.datetime.now()
        if self.data.get("0").get("year") != current.year or self.data.get("0").get("month") != current.month:
            fetching.dumpingToFile()
            reading = open(self.source, "r")
            self.data = json.load(reading)
        return self.data
        
    def generateNewLevel(self):
        self.checkFetching()
        correctAnswer = random.randint(1,self.top)
        answerLocation = random.randint(1,4)
        answerOption = []
        for x in range(4):
            if x == answerOption:
                answerOption.append(correctAnswer)
            else:
                while True:
                    randomAnswer = random.randint(1,self.top)
                    if randomAnswer not in self.answerOption:
                        answerOption.append(randomAnswer)
                        break
        answerOption.append(answerLocation)
        
    def getLevel(self,level):
        return self.levelList[level]
    
    def checkAnswer(self, input):
        return input == self.answerOption
            
        
    def testRun(self):
        """
        Only used to run test 
        """
        self.checkFetching()
        


test = Level()
test.testRun()