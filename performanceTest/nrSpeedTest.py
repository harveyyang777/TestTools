# -*- coding:utf-8 -*-
import os
import time
import re
HotStartList=[]
WarmStartList=[]
ColdStartList=[]
testPkg="com.mobilesrepublic.appy"
testActivity=".InitActviity"
count=3

def coldStartTest():
    os.popen("adb shell pm clear "+testPkg)
    time.sleep(1)
    startTimeMsg=os.popen("adb shell am start -W -n "+testPkg+"/"+testActivity).readlines()
    time.sleep(5)
    ColdStartList.append(startTimeMsgParser(startTimeMsg))

    os.popen("adb shell am force-stop "+testPkg)


def warmStartTest():
    os.popen("adb shell am force-stop"+testPkg)
    time.sleep(1)
    startTimemsg=os.popen("adb shell am start -W -n "+testPkg+"/"+testActivity).readlines()
    time.sleep(5)
    WarmStartList.append(startTimeMsgParser(startTimemsg))

    os.popen("adb shell am force-stop "+testPkg)

def hotStartTest():
    os.popen("adb shell am start -n "+testPkg+"/"+testActivity)
    os.popen("adb shell input keyevent 3")
    time.sleep(3)
    startTimemsg = os.popen("adb shell am start -W -n " + testPkg + "/" + testActivity).readlines()
    time.sleep(5)
    HotStartList.append(startTimeMsgParser(startTimemsg))
    os.popen("adb shell am force-stop " + testPkg)




#处理回调信息，返回waittime
def startTimeMsgParser(msg):
    total=0
    wait=0
    for i in msg:
        if re.match("WaitTime",str(i)):
            time=str(i).rstrip().split(": ")[1]
            wait=int(time)
            print i

        if re.match("TotalTime",str(i)):
            totaltime=str(i).rstrip().split(": ")[1]
            total=int(totaltime)
            print i

    return wait

def average(list):
    sum=0
    avg=0
    for i in list:
        sum=sum+i
    avg=sum/(len(list))
    return avg


def outPut():
    print  "cold:"+str(ColdStartList)
    print "cold average:"+str(average(ColdStartList))
    print  "warm:"+str(WarmStartList)
    print  "warm average:"+str(average(WarmStartList))
    print  "hot"+str(HotStartList)
    print  "hot average:" + str(average(HotStartList))




#start from here
os.popen("adb logcat -c")

for i in range (count):
    print "coldStart:"
    print ""
    coldStartTest()

os.popen("adb logcat -d -s ActivityManager |grep 'Display' >log/coldlog.txt")


os.popen("adb logct -c")
for i in range(count):
    print "warmStart:"
    print ""
    warmStartTest()

os.popen("adb logcat -d -s ActivityManager |grep 'Display'>log/warmlog.txt")

os.popen("adb logct -c")

for i in range(count):
    print "hotStart:"
    print ""
    hotStartTest()

os.popen("adb logcat -d -s ActivityManager |grep 'Display'>log/hotlog.txt")



