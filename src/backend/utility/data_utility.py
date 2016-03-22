
import numpy as np

from models.wafermap import WaferMap
import os




def generateData(data_dir) :
    smiley =[[28, 33], [31, 34], [64, 35], [55, 73], [36, 69], [22, 57], [27, 34], [29, 37], [63, 32], [74, 58], [66, 35], [64, 33], [65, 34], [44, 72], [62, 33], [66, 32], [42, 71], [65, 71], [29, 36], [67, 34], [63, 33], [62, 32], [71, 65], [28, 65], [73, 62], [23, 58], [63, 35], [53, 73], [28, 34], [70, 67], [65, 33], [66, 33], [28, 35], [48, 73], [57, 73], [70, 66], [67, 70], [21, 57], [23, 60], [62, 31], [31, 35], [47, 73], [56, 73], [63, 31], [65, 32], [24, 60], [75, 57], [51, 73], [29, 34], [29, 35], [73, 61], [30, 37], [64, 32], [45, 72], [28, 37], [65, 35], [22, 58], [30, 36], [64, 72], [31, 36], [63, 34], [73, 60], [49, 73], [30, 33], [72, 63], [66, 34], [23, 59], [28, 36], [62, 35], [69, 67], [59, 73], [69, 68], [60, 73], [62, 34], [25, 63], [75, 56], [30, 34], [62, 72], [64, 31], [74, 60], [39, 71], [24, 61], [25, 62], [33, 68], [61, 73], [54, 73], [68, 69], [58, 73], [66, 70], [26, 64], [75, 58], [67, 35], [72, 62], [27, 64], [63, 72], [29, 33], [27, 36], [64, 34], [27, 35], [74, 59], [30, 66], [72, 64], [31, 67], [30, 35], [71, 64], [67, 33]]
    # smiley = [[1, 15], [1, 18], [1, 20], [1, 12], [1, 10], [1, 17], [1, 16], [1, 19], [1, 22], [1, 14], [1, 6], [1, 2], [0, 21], [1, 1], [1, 5], [1, 23], [1, 0], [1, 9], [1, 7], [1, 8], [1, 11], [1, 4], [2, 22], [1, 3], [1, 21], [1, 13], [0, 20]]

    smiley.extend(smiley)

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


    for i in range(1,400):
        waferid = "wafer{0}".format(i)
        waferMap = WaferMap(waferid)
        rand = np.random.rand()
        if(rand > 0.75) :
            waferMap.initMap(100,100,pattern1)
            waferMap.setTitle("Pattern1")
        elif (rand > 0.5) :
            waferMap.initMap(100,100,pattern2)
            waferMap.setTitle("Pattern2")
        elif (rand > 0.25) :
            waferMap.initMap(100,100,pattern3)
            waferMap.setTitle("Pattern3")
        else :
            waferMap.initMap(100,100,smiley)
            waferMap.setTitle("Smiley")
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