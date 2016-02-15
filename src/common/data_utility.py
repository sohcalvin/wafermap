
import numpy as np

from models.wafermap import WaferMap
import os


dataDir = "data/"

def generateData() :
    # pattern1 = [[i,i] for i in (range(25,40))]
    pattern1 = [[i,i] for i in (range(25,35))]
    pattern1.extend(pattern1)
    pattern2 = [[i,i] for i in (range(26,40))]
    pattern2.extend(pattern2)
    for i in range(1,200):
        waferid = "wafer{0}".format(i)
        waferMap = WaferMap(waferid)
        # waferMap.initMap(100,100,pattern1)
        if(np.random.rand() > 0.5) :
            waferMap.initMap(100,100,pattern1)
            waferMap.setTitle("Pattern1")
        else :
            waferMap.initMap(100,100,pattern2)
            waferMap.setTitle("Pattern2")
        waferMap.save(dataDir + "{0}".format(waferid))



def loadData():
    outData = []
    for file_name in os.listdir(dataDir):
        waferMap = WaferMap.load(os.path.join(dataDir,file_name))
        bodyArray = waferMap.getBody()
        bodyOneLine = []
        for i in bodyArray :
            bodyOneLine.extend(i)
        outData.append([waferMap.getTitle(), bodyOneLine])

    return outData