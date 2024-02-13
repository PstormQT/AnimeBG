import json

from dataclasses import dataclass
@dataclass
class ImageData:
    name : str
    location :str
    
def openfile():
        imageinfo = []
        with open("animedatabase.txt") as file:
            for line in file:
                if line == "\n":
                    pass
                else:
                    line = line.split(" ")
                    location = str(line[0])
                    name = str(line[1])
                    imageinfo.append(ImageData(name,location))
        return imageinfo
    
def main():
    data = openfile()
    for picture in data:
        print("\"" + picture.name + "\"" + ":"  + "\""+picture.location+"\",")
        
        
def txtToJson():
    imageinfo = []
    with open("animedatabase.txt") as file:
        for line in file:
            if line  == "\n":
                pass
            else:
                line = line.split(" ")
                location = str(line[0])
                name = str(line[1])
                imageinfo.append(ImageData(name,location))
    with open("database.json","w") as jsonfile:
        imageinfo = json.dump(imageinfo,jsonfile)
        
txtToJson()