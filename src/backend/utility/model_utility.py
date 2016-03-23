

def buildNaiveBayesModel(X,Y) :
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X,Y)
    return classifier

def buildSVCModel(X, Y) :
    from sklearn.svm import SVC
    clf = SVC(probability=True)
    clf.fit(X, Y)
    # SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    # decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    # max_iter=-1, probability=False, random_state=None, shrinking=True,
    # tol=0.001, verbose=False)
    return clf

def buildLogRegressionModel(X, Y) :
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression(C=1e5)
    clf.fit(X, Y)
    return clf
# >>> print(clf.predict([[-0.8, -1]]))