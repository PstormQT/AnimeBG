import requests, json

class dataFetch:
    BASE_URL = "https://api.mangadex.org"
    MAX_FETCHING = 10
    outFileFull = "MangadexTop1000Full.json"
    offset = 0
    dataReq = ["cover_art"]
    followCount = "desc"
    fetchParam = {
        "includes[]" : dataReq,
        "order[followedCount]" : followCount,
        "offset" : offset,
        "limit" : MAX_FETCHING
    }
    mangadata = {}
        
        
    def dataFetching(self):
        self.mangadata = requests.get(f"{self.BASE_URL}/manga", params = self.fetchParam)
        self.mangadata = self.mangadata.json()["data"]

    
    def jsonDump(self):
        openOutFile = open(self.outFileFull,"w")
        json.dump(self.mangadata, openOutFile,indent=6)
        openOutFile.close()
        
    def getReqData(self):
        with open(self.outFileFull) as dataFile: 
            data = json.loads(dataFile)
            
            

def test():
    testcase = dataFetch()
    testcase.dataFetching()
    testcase.jsonDump()
    testcase.getReqData()
        
if __name__ == "__main__":
    test()
