import json, datetime, fetching, random

class Level:
    source = "MangadexTop1000Full.json"
    def __init__(self, leveldif : int, difficulty : int, time : int):
        """
        Indicate req leve

        Args:
            level (int): Level req
            difficulty (int): difficulty req
            time (int): Time Counter
        """
        self.leveldif = leveldif
        self.difficulty = difficulty
        self.time = time
        self.data = None
        self.level = []
        
    def __init__(self):
        """
        Overlaod the main class with default value
        """
        self.leveldif = 0
        self.difficulty = 0
        self.time = -1
        self.data = None
        self.level = []
    
    def checkFetching(self):
        """Fetching the json file recheck if needed"""
        reading = open(self.source, "r")
        self.data = json.load(reading)
        
        current = datetime.datetime.now()
        if self.data.get("0").get("year") != current.year or self.data.get("0").get("month") != current.month:
            fetching.dumpingToFile()
            reading = open(self.source, "r")
            self.data = json.load(reading)    
        
    def instanceLevel(self):
        return None
    def testRun(self):
        """
        Only used to run test 
        """
        self.checkFetching()
        


test = Level()
test.testRun()