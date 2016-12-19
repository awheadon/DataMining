import nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
import re
from scipy import *
import numpy as np
from scipy.sparse import *
from sklearn.naive_bayes import MultinomialNB
import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
def preprocessing(list_text):
    ps = PorterStemmer()
    for text in list_text:
        #remove puncuation, special chacters, numbers and short words.
	text = re.sub(r"(?:\@|'|https?\://)\S+", "", text)
        text = re.sub(r'[^\w\s]','',text)
        text = re.sub("\d+", "", text)
	#Word stemming
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
#Read in training and test data
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

vectorizer = CountVectorizer(stop_words='english')
#Count vectorize training and test documents
train_features = vectorizer.fit_transform(train_docs)
test_features = vectorizer.transform(test_docs)
#Use term frequecy to reweight more common words
tfidf_transformer = TfidfTransformer()
train_tfidf = tfidf_transformer.fit_transform(train_features)
train_docs = None
test+docs = None
#Uncomment to use Niave Bayes and comment out The three sgd to use
##nb = MultinomialNB()
##nb.fit(train_tfidf, lable)
##predictions = nb.predict(test_features)


sgd = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)
sgd.fit(train_tfidf, lable)
predictions = sgd.predict(test_features)


#print predictions
predictionList = predictions.tolist()
finalpredictionList = []
for entry in predictionList:
    finalpredictionList.append(int(entry))
predictionsList = None
#df = pandas.DataFrame(finalpredictionList)
#df.to_csv('Submission.csv',mode = 'a',header ='sentiment')
print finalpredictionList

