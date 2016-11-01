from pymongo import MongoClient
import unicodedata
import ast
import json
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
#requires mongopy and matplotlib to install use: pip install [matplotlib/mongopy]
def createPlot(title, col):
    days = [0,0,0,0,0,0,0,0,0,0,0]
    iterCount = 0
    dates = ["Oct 11", "Oct 12", "Oct 13", "Oct 14", "Oct 15", "Oct 16",
             "Oct 17", "Oct 18", "Oct 19", "Oct 20", "Oct 21"]
    while (iterCount < len(days)):
        days[iterCount] = col.find({ "created_at" : {'$regex': dates[iterCount]}}).count()
        iterCount += 1
 
    plt.plot(date, days, label=title)
    print "Created plot: " + title
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

CurrentSum = createPlot("Altcoin", altcoin)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Bitcoin", bitcoin)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Coindesk", coindesk)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Cryptocurrency", cryptocurrency)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Gold", gold)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Apple", appl)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Google", goog)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

CurrentSum = createPlot("Yahoo", yhoo)
sumDays = [x+y for x,y in zip(sumDays,CurrentSum)]
CurrentSum = None

plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.title('Tweets')
plt.legend()
plt.show()

plt.plot(date, sumDays, label="Total Tweets")
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.title('Number of Total Tweets')
plt.legend()
plt.show()

