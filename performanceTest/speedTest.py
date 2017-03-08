# -*- coding:utf-8 -*-
import os
import time
import re

'''

'''
#warmStart
nrTimeList=[]
topbuzzTimeList=[]

#coldStart
nrColdList=[]
topbuzzColdList=[]

#hotStart
nrHotList=[]
topbuzzHotList=[]
#获取一次topbuzz温启动时间
def topbuzzWarmStartTest():
    os.popen("adb shell am force-stop com.ss.android.article.master")
    time.sleep(2)
    msg=os.popen("adb shell am start -W -n com.ss.android.article.master/com.ss.android.article.pagenewark.activity.SplashActivity").readlines()
    time.sleep(2)
    value=0
    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "topbuzz_warm:"+str(m)

    os.popen("adb shell am force-stop com.ss.android.article.master")

    return value



#获取一次nr温启动时间
def NRWarmStartTest():

    value=0
    os.popen("adb shell am force-stop  com.mobilesrepublic.appy")
    time.sleep(2)
    msg = os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity").readlines()
    time.sleep(4)

    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "nr_warm:"+str(m)

    os.popen("adb shell am force-stop  com.mobilesrepublic.appy")
    return value


#获取一次nr冷启动时间
def NRColdStartTest():

    value=0
    os.popen("adb shell pm clear com.mobilesrepublic.appy")
    time.sleep(2)
    msg = os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity").readlines()
    time.sleep(4)

    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "nr_cold:"+str(m)

    os.popen("adb shell am force-stop  com.mobilesrepublic.appy")
    return value

#获取一次topbuzz冷启动时间
def topbuzzColdStartTest():
    os.popen("adb shell pm clear com.ss.android.article.master")
    time.sleep(2)
    msg=os.popen("adb shell am start -W -n com.ss.android.article.master/com.ss.android.article.pagenewark.activity.SplashActivity").readlines()
    time.sleep(2)
    value=0
    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "topbuzz_cold:"+str(m)

    os.popen("adb shell am force-stop com.ss.android.article.master")
    return value


#获取一次nr热启动时间
def NRHotTest():


    os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity")
    value=0
    os.popen("adb shell input keyevent 3")
    time.sleep(2)
    msg = os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity").readlines()
    time.sleep(4)

    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "nr_hot:"+str(m)

    os.popen("adb shell input keyevent 3")
    return value

#获取一次topbuzz热启动时间
def topbuzzHotStartTest():
    os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity")
    os.popen("adb shell input keyevent 3")
    time.sleep(2)
    msg=os.popen("adb shell am start -W -n com.ss.android.article.master/com.ss.android.article.pagenewark.activity.SplashActivity").readlines()
    time.sleep(2)
    value=0
    for m in msg:
        m = m.rstrip()
        flag = re.match("WaitTime", m)
        if flag:
            m = m.split(": ")
            value=int(m[1])
            print "topbuzz_hot:"+str(m)

    os.popen("adb shell input keyevent 3")
    return value


#输出温启动统计结果
def outputWarmStart():
    nrSum=0
    tbSum=0
   # print topbuzzTimeList
  #  print nrTimeList

    for elem in nrTimeList:
        nrSum = nrSum + elem
    # print "sum:"+str(sum)
    print "NR warmStart average:" + str(nrSum / len(nrTimeList))


    for elemt in topbuzzTimeList:
        tbSum = tbSum + elemt
        # print "sum:"+str(sum)
    print "TB warmStart average:" + str(tbSum / len(topbuzzTimeList))
    return

#输出冷启动统计结果
def outputColdStart():
    nrSum=0
    tbSum=0
  #  print topbuzzColdList
   # print nrColdList

    for elem in nrColdList:
        nrSum = nrSum + elem
    # print "sum:"+str(sum)
    print "NR coldStart average:" + str(nrSum / len(nrColdList))


    for elemt in topbuzzColdList:
        tbSum = tbSum + elemt
        # print "sum:"+str(sum)
    print "TB coldStart average:" + str(tbSum / len(topbuzzColdList))
    return

#输出热启动统计结果
def outputHotStart():
    nrSum=0
    tbSum=0
  #  print topbuzzColdList
   # print nrColdList

    for elem in nrHotList:
        nrSum = nrSum + elem
    # print "sum:"+str(sum)
    print "NR HotStart average:" + str(nrSum / len(nrHotList))


    for elemt in topbuzzHotList:
        tbSum = tbSum + elemt
        # print "sum:"+str(sum)
    print "TB hotStart average:" + str(tbSum / len(topbuzzHotList))
    return




#os.popen("adb shell screenrecord /sdcard/speedtest.mp4")

#测试冷启动次数
for i in range(3):
    time.sleep(1)
    topbuzzColdList.append(topbuzzColdStartTest())
    time.sleep(1)
    nrColdList.append(NRColdStartTest())

#测试温启动
for i in range(3):
    time.sleep(1)
    topbuzzTimeList.append(topbuzzWarmStartTest())
    time.sleep(1)
    nrTimeList.append(NRWarmStartTest())


#测试热启动
for i in range(3):
    time.sleep(1)
    topbuzzHotList.append(topbuzzHotStartTest())
    time.sleep(1)
    nrHotList.append(NRHotTest())


outputWarmStart()
outputColdStart()
outputHotStart()




