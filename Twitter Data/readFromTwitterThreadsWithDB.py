import tweepy
import json
from pymongo import MongoClient
from threading import Thread
#requires mongopy and tweepy to install use: pip install [tweepy/mongopy]
con = MongoClient('localhost', 27017)
db = con.streamData
altcoin = db.altcoin
bitcoin = db.bitcoin
coindesk = db.coindesk
cryptocurrency = db.cryptocurrency
gold = db.gold
appl = db.appl
goog = db.goog
yhoo = db.yhoo

ckey = 'fJGz2D1SA2wanOlMlRpl3jvlN'
csecret = 'wfrYII7UDrUjibiKjLYU14ZyI3zP6oaIpFi7XKkKF6UkjqoWct'
atoken = '784761028592664577-wMQOmwJKz3LIn0haBOafk5dm1WI1pAU'
asecret = 'RPGOSD8mw7D0dmWwcWQWnjIEhXLaTLPX4Z4AYbDPYFwS5'    
    
class StreamListener(tweepy.StreamListener):
    def __init__(self, keyword, api=None):
        super(StreamListener, self).__init__(api)
        self.keyword = keyword

    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        #print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        tweet = json.loads(data)
        username = tweet["user"]["screen_name"] + " " + self.keyword
        print username
        if self.keyword=='altcoin':
            altcoin.insert(tweet)
        elif  self.keyword=='bitcoin':
            bitcoin.insert(tweet)
        elif  self.keyword=='coindesk':
            coindesk.insert(tweet)
        elif  self.keyword=='cryptocurrency':
            cryptocurrency.insert(tweet)
        elif  self.keyword=='gold':
            gold.insert(tweet)
        elif  self.keyword=='appl':
            appl.insert(tweet)
        elif  self.keyword=='goog':
            goog.insert(tweet)
        else:
            yhoo.insert(tweet)
        #print 'Ok, this is actually running'


def start_stream(auth, track):
    tweepy.Stream(auth=auth, listener=StreamListener(track)).filter(track=[track])


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

track = ['altcoin','bitcoin','coindesk','cryptocurrency','gold','appl','goog','yhoo']
for item in track:
    thread = Thread(target=start_stream, args=(auth, item))
    thread.start()
