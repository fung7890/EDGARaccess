import re

list1 = []
fullList = []

f = open("output2016.csv", "r")

contents = f.readlines()

for line in contents:
    list1.append((re.search('data/(.+?)/', line)).group(1))
    list1.append((re.search('([^/]+)/?$', line)).group(1).replace(".txt","").replace(" ",""))
    fullList.append(list1[:])
    list1.clear()


print(fullList[0])