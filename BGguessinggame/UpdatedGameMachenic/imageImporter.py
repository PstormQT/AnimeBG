import json, os

class imageImporter:
    def __init__(self,file,dir):
        self.file = file
        self.dir = dir
        self.jsondatabase = {}
        
    def parse(self):
        counter = 0
        for root, dirs, files in os.walk(self.dir):
            if counter == 0:
                counter += 1
            else: 
                self.jsondatabase[root] = files
                
    def jsonDump(self):
        outFile = open(self.file,"w")
        json.dump(self.jsondatabase, outFile, indent=6)
            
            
def main():
    test = imageImporter("database.json",".\\image")
    test.parse()
    test.jsonDump()
                               
if __name__ == "__main__":
    main()