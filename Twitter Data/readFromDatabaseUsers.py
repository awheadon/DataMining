from pymongo import MongoClient
import unicodedata
import ast
import json
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
import itertools
#requires mongopy and matplotlib to install use: pip install [matplotlib/mongopy]
#Takes some time because of large number of tweets status is shown in console
def checkExist(tweetUser, users):
    x = 0
    while(x<len(users)):
        #print users[x] + ' ' + str(x) + ' ' + tweetUser
        if users[x] == tweetUser:
            return True
        x+=1
    return False


def createPlot(test, name):
    days = [0,0,0,0,0,0,0,0,0,0,0]
    test, test2 = itertools.tee(test)
    users = []
    for tweet in test:
        currentUser = tweet['user']['screen_name']
       
        if(not(currentUser in users)):
            users.append(currentUser)


    for tweet2 in test2:
        stringTweet = unicodedata.normalize('NFKD', tweet2['created_at']).encode('ascii', 'ignore')
        if ("Oct 11" in stringTweet) and checkExist(tweet2['user']['screen_name'], users):
            days[0] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 12" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[1] += 1
            users.append("1")
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 13" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[2] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 14" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[3] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 15" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[4] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 16" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[5] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 17" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[6] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 18" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[7] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 19" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[8] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 20" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[9] += 1
            users.remove(tweet2['user']['screen_name'])
        elif "Oct 21" in stringTweet and checkExist(tweet2['user']['screen_name'], users):
            days[10] += 1
            users.remove(tweet2['user']['screen_name'])
        else:
            pass
    plt.plot(date, days, label=name)
    print name + ' Done'
    return days;



firstDay = dt.date(2016,10,11)
date = [firstDay + dt.timedelta(days=x) for x in range(0,11)]
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(dates.DayLocator())
sumDays = [0,0,0,0,0,0,0,0,0,0,0]


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

test = altcoin.find()
CurrentSum = createPlot(test, "Altcoin")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = bitcoin.find()
CurrentSum = createPlot(test, "Bitcoin")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = coindesk.find()
CurrentSum = createPlot(test, "Coindesk")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = cryptocurrency.find()
CurrentSum = createPlot(test, "Cryptocurrency")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = gold.find()
CurrentSum = createPlot(test, "Gold")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = appl.find()
CurrentSum = createPlot(test, "appl")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = goog.find()
CurrentSum = createPlot(test, "goog")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None
test = yhoo.find()
CurrentSum = createPlot(test, "yhoo")
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)] 
CurrentSum = None
test = None

plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of Users')
plt.title('Users')
plt.legend()
plt.show()
plt.plot(date, sumDays, label="Number of Total Users")
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of Users')
plt.title('Tweets')
plt.legend()
plt.show()
