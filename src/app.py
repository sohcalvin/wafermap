import pandas as pd
import numpy as np

from models.wafermap import WaferMap
import os
import json

dataDir = "data/"

def generateData() :
    # pattern1 = [[i,i] for i in (range(25,40))]
    pattern1 = [[i,i] for i in (range(1,2))]
    for i in range(1,10):
        waferid = "wafer{0}".format(i)
        waferMap = WaferMap(waferid, title="Pattern1")
        # waferMap.initMap(100,100,pattern1)
        waferMap.initMap(5,5,pattern1)
        waferMap.save(dataDir + "{0}".format(waferid))



def loadData():
    outData = []
    for file_name in os.listdir(dataDir):
        waferMap = WaferMap.load(os.path.join(dataDir,file_name))
        bodyArray = waferMap.getBody()
        bodyOneLine = []
        for i in bodyArray :
            bodyOneLine.extend(i)
        outData.append(bodyOneLine)
    return outData

# generateData()

dataOneLinePerMap = loadData()
pandaDataMaps = pd.DataFrame(dataOneLinePerMap)

print(pandaDataMaps)






# waferMap2 = WaferMap.load("t.txt")

# jsonData = waferMap2.jsonData();
# print(json.dumps(jsonData))


