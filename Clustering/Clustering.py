##It will take a long time to get the proper answer 
import re
import nltk
from nltk.stem.porter import PorterStemmer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


df = pd.read_csv('Documents.csv', header=0)
documents = df.SMS

print documents[0]
parsedString = []
ps = PorterStemmer()
num_k = 2
for text in documents:
    text = re.sub(r"(?:\@|'|https?\://)\S+", "", text)  # delete punctuation
    text = re.sub(r'[^\w\s]','', text)  # delete punctuation
    text = re.sub("\d+", "", text)  # remove number from text

    
    parsedString.append(text)
    #print parsedString
    
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(parsedString)
count = 0;
while(count<3):
    count = 0;
    true_k = 2
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=20, verbose=1)
    model.fit(X)





    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print "Cluster %d:" % i,
        for ind in order_centroids[i, :10]:
            if(i == 0 and (terms[ind]=="free" or terms[ind]=="claim" or terms[ind]=="prize" or terms[ind]=="urgent" or terms[ind]=="won")):
                count+= 1;
            print ' %s' % terms[ind],
        print
    i = 0
    #print X.shape
    hrlp= model.labels_.tolist()
    for l in hrlp:
        if l == 1:
            i+=1
            
    print hrlp
    print count
