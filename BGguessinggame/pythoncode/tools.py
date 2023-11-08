# def main():
#     for x in range(1,14):
#         print("image\\\\Bunnygirlsenpai\\\\bunnygirlsenpai"+ str(x) +".webp Rascle_does_not_dream_of_")
# if __name__ == '__main__':
#     main()
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
        
main()