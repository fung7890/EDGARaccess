import os, sys
from urllib.request import urlretrieve
import urllib

year = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016" ]
qtr = ["QTR1", "QTR2", "QTR3", "QTR4",] 


def grab():
    
    for i in range(len(year)):           
        for k in range(len(qtr)):
            path = "https://www.sec.gov/Archives/edgar/full-index/%s/%s/company.idx" % (year[i], qtr[k]) 
            try:
                urlretrieve(path, "CompanyCodes/%s%s.txt" % (year[i], qtr[k]))
            except:
                print("doesn't exist")    
              
def createFolders():
    
    for i in range(len(year)):              
        path = "./%sCompanyCodes" % (year[i])
        os.mkdir(path)


grab()