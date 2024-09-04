import pygame
from io import BytesIO
import requests
from PIL import Image
import random

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

def pinkRandomOmit(start, stop, emit):
    """Pick a random number in a range without certain item in a list

    Args:
        start (int): Starting point
        stop (int): Ending point
        emit (set - int): Set of int to be excluded 

    Returns:
        _type_: _description_
    """
    while True:
        random = random.randint(start,stop)
        if (random not in emit):
            return random 