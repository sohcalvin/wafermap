
import numpy as np

from models.wafermap import WaferMap
import os




def generateData(data_dir) :
    pattern1 = [[i,i] for i in (range(25,65))]
    pattern1.extend(pattern1)

    pattern2 = [[i,i] for i in (range(26,65))]
    pattern2.extend(pattern2)

    pattern1 = []
    for i in (range(25,65)):
        if(i < 45) :
            pattern1.append([i+5,i])
        else :
            pattern1.append([i-5,i])
    pattern1.extend(pattern1)
    # pattern1 = [[val+i*2,val] for i,val in enumerate(range(25,35), 1)]

    for i in range(1,200):
        waferid = "wafer{0}".format(i)
        waferMap = WaferMap(waferid)
        if(np.random.rand() > 0.5) :
            waferMap.initMap(100,100,pattern1)
            waferMap.setTitle("Pattern1")
        else :
            waferMap.initMap(100,100,pattern2)
            waferMap.setTitle("Pattern2")
        waferMap.save(data_dir + "/{0}".format(waferid))



def loadData(data_dir):
    outData = []
    for file_name in os.listdir(data_dir):
        waferMap = WaferMap.load(os.path.join(data_dir,file_name))
        bodyArray = waferMap.getBody()
        bodyOneLine = []
        for i in bodyArray :
            bodyOneLine.extend(i)
        outData.append([waferMap.getTitle(), bodyOneLine])

    return outData