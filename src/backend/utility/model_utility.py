

def buildNaiveBayesModel(X,Y) :
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X,Y)
    return classifier