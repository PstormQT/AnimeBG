import pygame
from io import BytesIO
import requests
from PIL import Image
import random
import datetime
import json
import assets.classesAndUtil.fetching as fetching

source = "MangadexTop1000Full.json"

def opeingPhoto(mangaID, mangaLink):
    """_summary_

    Args:
        mangaID (String): The mangaID
        mangaLink (String): The tail link of manga
    """
    rsp = requests.get("https://uploads.mangadex.org/covers/" + mangaID + "/" + mangaLink + ".512.jpg")
    pilimage = Image.open(BytesIO(rsp.content)).convert("RGBA")
    pgimg = pygame.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)
    return pgimg

def pickRandomOmit(start, stop, emit):
    """Pick a random number in a range without certain item in a list

    Args:
        start (int): Starting point
        stop (int): Ending point
        emit (set - int): Set of int to be excluded 

    Returns:
        _type_: _description_
    """
    while True:
        randomNumber = random.randint(start,stop)
        if (random not in emit):
            return randomNumber 
        
        
def checkFetching():
        """Fetching the json file recheck if needed"""
        reading = open(source, "r")
        data = json.load(reading)
        
        current = datetime.datetime.now()
        if data.get("0").get("year") != current.year or data.get("0").get("month") != current.month:
            fetching.dumpingToFile()
            reading = open(source, "r")
            data = json.load(reading)