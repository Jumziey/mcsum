import urllib.request
import time
def getResponseCode(url):
    try:
        conn = urllib.request.urlopen(url)
        return conn.getcode()
    except urllib.error.HTTPError:
        return "0"


years = 16
months = 12-1 #remember +1
days = 31-1 #remember +1
tests = [""];
for y in range(years):
    for m in range(months):
        for d in range(days):
            if y<10:
                year = "0" + str(y)
            else:
                year = str(y)

            if (m+1)<10:
                month = "0" + str(m+1)
            else:
                month = str(m+1)

            if(d+1)<10:
                day = "0" + str(d+1)
            else:
                day = str(d+1)

            tests.append("t"+year+month+day + ".pdf")
            tests.append("t"+year+month+day + ".dvi")
            tests.append("t"+year+month+day + ".txt")
            tests.append("t"+year+month+day + ".tex")

#for test in tests:

testurl = ["http://www.google.se", "https://docs.python.org/3.0/library/random.html", "http://google.se/aoeuhtnasoeuhtnsaoeu"]
for url in testurl:
    code = getResponseCode(url)
    if code == 200:
        print(url +" works!");

#print(getResponseCode("http://www.tp.umu.se/mc"))
