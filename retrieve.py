from urllib.request import urlretrieve
import os, sys
import urllib
import re
import glob
import pandas as pd
import numpy as np


list1 = []
fullList = []
year = ["2016","2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016" ]
qtr = ["QTR1", "QTR2", "QTR3", "QTR4",] 
fileList = glob.glob('10-kCodes/*.txt')

def retrieve():
    # for i in range(len(year)):
    #     with open("10-kCodes/10k%s%s.txt" % (year[i], qtr[0]), "r") as f:

    #         for line in f:
    #             print(line)


    for i in range(1): 
        for k in range(1): 
            with open("10-kCodes/10k%s%s.txt" % (year[i], qtr[k]), "r") as f:
             
                for line in f:
                               
                    # list1.append((re.search('data/(.+?)/', line)).group(1))
                    # list1.append((re.search('([^/]+)/?$', line)).group(1).replace(".txt","").replace(" ","").replace("\n","").replace("-",""))
                    # fullList.append(list1[:])
                    # list1.clear()

                    x = (re.search('data/(.+?)/', line)).group(1)
                    y = (re.search('([^/]+)/?$', line)).group(1).replace(".txt","").replace(" ","").replace("\n","").replace("-","")
                    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/Financial_Report.xlsx' % (x, y)
                    print(url)
                    try:
                        urlretrieve(url, "CompanyData/%s.csv" % (x))
                    except:
                        print("doesn't exist")



                # for p in range(5):
                #     url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/Financial_Report.xlsx' % (fullList[p][0],fullList[p][1])
                #     try:
                #         urlretrieve(url, "CompanyData/%s.csv" % (fullList[p][0]))
                #     except:
                #         print("doesn't exist")



# def createFolders():
    
#     for i in range(len(year)):              
#         path = "CompanyData/%s" % (year[i])
#         os.mkdir(path)


retrieve()