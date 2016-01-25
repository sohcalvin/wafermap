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
        outData.append([waferMap.getTitle(), bodyOneLine])

    return outData

def buildNaiveBayesModel(X,Y) :
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X,Y)
    return classifier

# generateData()

dataOneLinePerMap = loadData()
maps = dataOneLinePerMap[1:]
print(maps)
pandaDataMaps = pd.DataFrame(dataOneLinePerMap)
pandaDataMaps.columns =["pattern", "body"]
X = pandaDataMaps['body'].values
X2 = pd.DataFrame(X)

Y = pandaDataMaps['pattern'].values

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=4)

print("Data Set Shapes trainX%s trainY%s testX%s testY%s" %(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape))

# model = buildNaiveBayesModel(X_train, Y_train)
# train_pred = model.predict(X_train)
# test_pred = model.predict(X_test)
# print("Prediction score is " , model.score(X,Y))
# from sklearn import metrics
# print( "Train Accuracy :", metrics.accuracy_score(Y_train, train_pred))
# print( "Test Accuracy :", metrics.accuracy_score(Y_test, test_pred))
# print(X)
# print(X2)
# print(Y)







# waferMap2 = WaferMap.load("t.txt")

# jsonData = waferMap2.jsonData();
# print(json.dumps(jsonData))


