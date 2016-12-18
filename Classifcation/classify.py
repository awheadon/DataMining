import nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
import re
from scipy import *
import numpy as np
from scipy.sparse import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

def preprocessing(list_text):
    ps = PorterStemmer()
    for text in list_text:
        text = re.sub(r"(?:\@|'|https?\://)\S+", "", text)
        text = re.sub(r'[^\w\s]','',text)
        text = re.sub("\d+", "", text)
        tokens = nltk.word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        tokens = [w for w in tokens if len(w) > 2]
        text = ""
        for token in tokens:
            stems = ps.stem(token)
            #print stems
            text += stems + " "
        #print text

        #print "################################################################################"
    #print "Preprossing Complete"
    return list_text

train_docs = []
test_docs = []
lable = []
with open ("TrainDataset.tsv", "rb") as train_file:
    count = 0
    lines = train_file.readlines()
    for line in lines:
        if count != 0:
            y= line.split()[1].replace('"','')
            lable.append(y)
            review = line.split(None, 1)[1].replace('"','')
            train_docs.append(review)
        count += 1

print len(train_docs)
print len(lable)

with open ("TestDataset.tsv", "rb") as test_file:
    count = 0
    lines = test_file.readlines()
    for line in lines:
        if count != 0:
            review = line.split(None, 1)[1].replace('"','')
            test_docs.append(review)
        count += 1

print len(train_docs) + len(test_docs)

train_docs = preprocessing(train_docs)
test_docs = preprocessing(test_docs)
print "Preprossing Complete"

vectorizer = TfidfVectorizer(min_df=5, max_df = 0.8, sublinear_tf=True, use_idf=True)
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform(train_docs)
test_features = vectorizer.transform(test_docs)

nb = MultinomialNB()
nb.fit(train_features, lable)

predictions = nb.predict(test_features)

predictionList = predictions.tolist()
finalpredictionList = []
for entry in predictionList:
    finalpredictionList.append(int(entry))
print finalpredictionList
