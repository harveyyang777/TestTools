# -*- coding:utf-8 -*-
import re

coldMainActivityList=[]
coldNewsActivityList=[]

hotMainActivityList=[]
hotNewsActivityList=[]

warmMainActivityList=[]
warmNewsActivityList=[]

def clear(s):
    info=s.split(": ")
  #  print info
    actity=info[1].split("/")[1]
    time=info[2]
    print  actity+":"+time
    return actity+":"+time

def secondsToMs(list):
    for i in list:
        if re.match("\ds",str(i)):
            seconds=str(i)[0]
            ms=




f_result=open("result/results.txt","w")

f_cold=open("log/coldlog.txt")
f_hot=open("log/hotlog.txt")
f_warm=open("log/warmlog.txt")

try:
    cold_lines=f_cold.readlines()
    hot_lines=f_hot.readlines()
    warm_lines=f_warm.readlines()

    print "cold:"
    for i in cold_lines:
        resultinfo=clear(i.rstrip())
        if re.search("com.cmcm.newsindia.MainActivity",resultinfo):
            time=resultinfo.split(":+")[1].split(" (")[0]
            coldMainActivityList.append(time)
        if re.search("com.cmcm.onews.ui.NewsActivity",resultinfo):
            time=resultinfo.split("+")[1]
            coldNewsActivityList.append(time)


    print coldMainActivityList
    print coldNewsActivityList

    print "hot:"
    for i in hot_lines:
        resultinfo = clear(i.rstrip())
        if re.search("com.cmcm.newsindia.MainActivity", resultinfo):
            time = resultinfo.split(":+")[1].split(" (")[0]
            hotMainActivityList.append(time)
        if re.search("com.cmcm.onews.ui.NewsActivity", resultinfo):
            time = resultinfo.split("+")[1]
            hotNewsActivityList.append(time)


    print hotMainActivityList
    print hotNewsActivityList
    print "warm:"
    for i in warm_lines:
        resultinfo = clear(i.rstrip())
        if re.search("com.cmcm.newsindia.MainActivity", resultinfo):
            time = resultinfo.split(":+")[1].split(" (")[0]
            warmMainActivityList.append(time)
        if re.search("com.cmcm.onews.ui.NewsActivity", resultinfo):
            time = resultinfo.split("+")[1]
            warmNewsActivityList.append(time)
    print warmMainActivityList
    print warmNewsActivityList

    secondsToMs(coldMainActivityList)

finally:
    f_cold.close()
    f_hot.close()
    f_warm.close()


'''
try:
    f_result.write("test3")

finally:
    f_result.close()
'''




