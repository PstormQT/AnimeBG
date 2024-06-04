import requests, json, datetime

BASE_URL = "https://api.mangadex.org"
MAX_FETCHING = 20
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
altTitleKey = "en"


def dumpingToFile():
    """
    Parsing through the data and filer through the attribute
    """
    openOutFile = open(outFileFull,"w")
    data = parser()
    dataDumps = {}
    current = datetime.datetime.now()
    "reserving slot 0 for data update"
    dataDumps[0] = {"year": current.year, "month": current.month, "fetchCount" : MAX_FETCHING}
    
    counter = 1
    for entries in data.get("data"):
        entry = {}
        
        "Adding Manga ID"
        entry["id"] = entries.get("id")
        
        "Adding main title"
        title = entries.get("attributes").get("title")
        for value in title.values():
            entry["title"] = value
            

        "Adding alt title in"
        for altTiles in entries.get("attributes").get("altTitles"):
            if altTitleKey in altTiles:
                entry["alt-title"] = altTiles.get(altTitleKey)
                break
        if entry.get("alt-title") == None:
            entry["alt-title"] = ""
        
        
        "Adding author id in"
        for member in entries.get("relationships"):
            if member.get("type") == "author":
                entry["author"] = member.get("id")
                break

        "Adding cover id in"
        for member in entries.get("relationships"):
            if member.get("type") == "cover_art":
                entry["coverArt"] = member.get("attributes").get("fileName")
                break
        dataDumps[counter] = entry
        counter += 1
    
    json.dump(dataDumps, openOutFile,indent=6)
    


def getAuthor(id):
    """
    Util function for author look up

    Args:
        id (int): the author id

    Returns:
        Str: Author name / description
    """
    authorLinkLoopup = BASE_URL + "/author/" + id
    authorData = requests.get(authorLinkLoopup).json()
    return authorData

def parser():
    """
    Parsing data from mangadex

    Returns:
        dict: data of reading JSON files
    """
    mangaData = requests.get(f"{BASE_URL}/manga", params = fetchParam)
    mangaDataJson = mangaData.json()
    
    
    return mangaDataJson
    
if __name__ == "__main__":
    dumpingToFile()
