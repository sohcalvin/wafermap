import pandas as pd
import numpy as np
from common.data_utility import generateData
from common.data_utility import loadData

from models.wafermap import WaferMap
import os
import json

def buildNaiveBayesModel(X,Y) :
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X,Y)
    return classifier

# generateData()

dataOneLinePerMap = loadData()
tmp = [i[1] for i in dataOneLinePerMap]
X = pd.DataFrame(tmp)
Y = np.array([i[0] for i in dataOneLinePerMap])


from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=4)

print("Data Set Shapes trainX%s trainY%s testX%s testY%s" %(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape))

model = buildNaiveBayesModel(X_train, Y_train)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)
print("Prediction score is " , model.score(X,Y))
from sklearn import metrics
print( "Train Accuracy :", metrics.accuracy_score(Y_train, train_pred))
print( "Test Accuracy :", metrics.accuracy_score(Y_test, test_pred))
# print(X)
# print(Y)







# waferMap2 = WaferMap.load("t.txt")

# jsonData = waferMap2.jsonData();
# print(json.dumps(jsonData))


