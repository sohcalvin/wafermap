
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
        offset =4
        if(i < 45) :
            pattern1.append([i+offset,i])
        else :
            pattern1.append([i-offset,i])
    pattern1.extend(pattern1)

    pattern3 = [[i,i] for i in (range(65, 85))]
    pattern3.extend(pattern3)


    for i in range(1,200):
        waferid = "wafer{0}".format(i)
        waferMap = WaferMap(waferid)
        rand = np.random.rand()
        if(rand > 0.677) :
            waferMap.initMap(100,100,pattern1)
            waferMap.setTitle("Pattern1")
        elif (rand > 0.333) :
            waferMap.initMap(100,100,pattern2)
            waferMap.setTitle("Pattern2")
        else :
            waferMap.initMap(100,100,pattern3)
            waferMap.setTitle("Pattern3")
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