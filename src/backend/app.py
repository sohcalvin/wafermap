import pandas as pd
import numpy as np
from utility.data_utility import generateData,readSeedPattern
from utility.data_utility import loadData
from utility.model_utility import buildNaiveBayesModel, buildSVCModel, buildLogRegressionModel

import os
import pickle

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "../../data")
TRAINING_MAP_DIR = os.path.join(DATA_DIR,"training_maps")
PATTERN_DIR = os.path.join(DATA_DIR,"patterns")

seed_pattern_dict = readSeedPattern(PATTERN_DIR)
generateData(TRAINING_MAP_DIR, seed_pattern_dict,number_per_pattern=200)
# exit()


dataOneLinePerMap = loadData(TRAINING_MAP_DIR)
print(dataOneLinePerMap[0]) # First row
print(dataOneLinePerMap[1]) # Second row

tmp = [i[1] for i in dataOneLinePerMap]

X = pd.DataFrame(tmp) # Array of maplines
Y = np.array([i[0] for i in dataOneLinePerMap])
# model = buildNaiveBayesModel(X, Y)
# model = buildSVCModel(X, Y)
model = buildLogRegressionModel(X, Y)

pickle.dump(model,open("model.p","wb"))
def do_train_split():
    from sklearn.cross_validation import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=4)

    print("Data Set Shapes trainX%s trainY%s testX%s testY%s" %(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape))

    trainsplit_model = buildNaiveBayesModel(X_train, Y_train)
    train_pred = trainsplit_model.predict(X_train)
    test_pred = trainsplit_model.predict(X_test)
    print("Prediction score is " , trainsplit_model.score(X,Y))
    from sklearn import metrics
    print( "Train Accuracy :", metrics.accuracy_score(Y_train, train_pred))
    print( "Test Accuracy :", metrics.accuracy_score(Y_test, test_pred))











# waferMap2 = WaferMap.load("t.txt")

# jsonData = waferMap2.jsonData();
# print(json.dumps(jsonData))


