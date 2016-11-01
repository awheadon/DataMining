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
    
    days[0] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 11"}}))
    days[1] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 12"}}))
    days[2] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 13"}}))
    days[3] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 14"}}))
    days[4] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 15"}}))
    days[5] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 16"}}))
    days[6] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 17"}}))
    days[7] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 18"}}))
    days[8] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 19"}}))
    days[9] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 20"}}))
    days[10] = len(col.distinct("user.screen_name", { "created_at" : {'$regex': "Oct 21"}}))
    
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

