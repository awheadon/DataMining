from pymongo import MongoClient
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
#requires mongopy and matplotlib to install use: pip install [matplotlib/mongopy]
def createPlot(test, name):
    days = [0,0,0,0,0,0,0,0,0,0,0]
    for tweet in test:
        stringTweet = unicodedata.normalize('NFKD', tweet['created_at']).encode('ascii', 'ignore')
        if "Oct 11" in stringTweet:
            days[0] += 1
        elif "Oct 12" in stringTweet:
            days[1] += 1
        elif "Oct 13" in stringTweet:
            days[2] += 1
        elif "Oct 14" in stringTweet:
            days[3] += 1
        elif "Oct 15" in stringTweet:
            days[4] += 1
        elif "Oct 16" in stringTweet:
            days[5] += 1
        elif "Oct 17" in stringTweet:
            days[6] += 1
        elif "Oct 18" in stringTweet:
            days[7] += 1
        elif "Oct 19" in stringTweet:
            days[8] += 1
        elif "Oct 20" in stringTweet:
            days[9] += 1
        elif "Oct 21" in stringTweet:
            days[10] += 1
        else:
            print "nothing"
    plt.plot(date, days, label=name)
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
plt.ylabel('Number of Tweets')
plt.title('Tweets')
plt.legend()
plt.show()
plt.plot(date, sumDays, label="Total")
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.title('Tweets')
plt.legend()
plt.show()
