import urllib.request
import time
import datetime
import calendar
import os

def getResponseCode(url):
    try:
        conn = urllib.request.urlopen(url)
        return conn.getcode()
    except urllib.error.HTTPError:
        return "0"

def tests(years, months, days, endings):
    filenames = [""];
    for y in years:
        for m in months:
            for d in days:
                if y<10:
                    year = "0" + str(y)
                else:
                    year = str(y)

                if (m)<10:
                    month = "0" + str(m)
                else:
                    month = str(m+1)

                if(d)<10:
                    day = "0" + str(d)
                else:
                    day = str(d)

                if( calendar.monthrange(2000+y, m)[1]  >= d):
                    if(datetime.datetime(2000 + y, m, d).weekday() != 6):
                        for ending in endings:
                            filenames.append("t"+year+month+day + "." + ending)
    return filenames

years = [16]
days = list(range(1,31))
months = [6,5,8,2]
endings = [
    "pdf",
    "dvi",
    "txt",
    "tex"
]
'''
t = tests(years, months, days, endings)
for test in t:
    print(test, end='\r')
print()
print(len(t))
time.sleep(2)
exit()'''
for test in tests(years, months, days, endings):
    url = "an adress you wanna scrape" + test
    code = getResponseCode(url)
    #print(code);
    print(url, end='\r')
    if code == 200:
        print()
        print(url +" works!");
