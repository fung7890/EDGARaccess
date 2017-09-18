import os, sys

year = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016" ]
qtr = ["QTR1", "QTR2", "QTR3", "QTR4",] 

def extract():

    for i in range(len(year)):
        for k in range(len(qtr)):
            fo = open("CompanyCodes/%s%s.txt" % (year[i], qtr[k]), "r")
            f = open("10-kCodes/10k%s%s.txt" % (year[i], qtr[k]), "w")

            x = "10-K"
            for line in fo.readlines():
                if x in line:
                    f.write(line)




extract()    



# for filename in os.listdir("D:\Python\CompanyCodes"):  <-every file in folder









# from urllib.request import urlretrieve
# import os, sys
# import urllib
# import re


# list1 = []
# fullList = []
# year = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016" ]
# qtr = ["QTR1", "QTR2", "QTR3", "QTR4",] 


# def retrieve():
    
#     with open("10-kCodes/10k%s%s.csv" % (year[0], qtr[0]), "r") as f:
#         for line in f:
#             print(line)


    # for i in range(len(year)): 
    #     for k in range(len(qtr)): 
    #         with open("10-kCodes/10k%s%s.csv" % (year[i], qtr[k]), "r") as f:
    #             # print(f.readline())
    #             for h in f:
    #                 print(h)

                # for line in f:
                #     print(line)
                
                #     list1.append((re.search('data/(.+?)/', line)).group(1))
                #     list1.append((re.search('([^/]+)/?$', line)).group(1).replace(".txt","").replace(" ","").replace("\n","").replace("-",""))
                #     fullList.append(list1[:])
                #     list1.clear()


                # for p in range(5):
                #     url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/Financial_Report.xlsx' % (fullList[p][0],fullList[p][1])
                #     try:
                #         urlretrieve(url, "CompanyData/%s/%s.csv" % (year[i], fullList[p][0]))
                #     except:
                #         print("doesn't exist")



# def createFolders():
    
#     for i in range(len(year)):              
#         path = "CompanyData/%s" % (year[i])
#         os.mkdir(path)


# retrieve()







# list1 = []
# fullList = []


# # [cik, doc]
# ref = ["37996", "000003799617000068"]

# f = open("output2016.csv", "r")

# contents = f.readlines()

# for line in contents:
#     list1.append((re.search('data/(.+?)/', line)).group(1))
#     list1.append((re.search('([^/]+)/?$', line)).group(1).replace(".txt","").replace(" ","").replace("\n","").replace("-",""))
#     fullList.append(list1[:])
#     list1.clear()


# for i in range(5):
#     url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/Financial_Report.xlsx' % (fullList[i][0],fullList[i][1])
#     try:
#         urlretrieve(url, "2016CompanyData/%s.csv" % (fullList[i][0]))
#     except:
#         print("doesn't exist")

    

# len(fullList) replace this with range to get all data