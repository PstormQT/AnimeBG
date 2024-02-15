import requests, json

class dataFetch:
    BASE_URL = "https://api.mangadex.org"
    MAX_FETCHING = 10
    outfile = "MangadexTop1000.json"
    offset = 0
    dataReq = ["cover_art", "manga"]
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
        openOutFile = open(self.outfile,"w")
        json.dump(self.mangadata, openOutFile,indent=6)
        

def test():
    testcase = dataFetch()
    testcase.dataFetching()
    testcase.jsonDump()
        
if __name__ == "__main__":
    test()
