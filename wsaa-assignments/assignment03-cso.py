import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset): # function to that the pulled data and write to a file and save as json.
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset): # function to pull the data from the URL in json format
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    getAllAsFile("FIQ02")