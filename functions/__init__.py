# -*- coding:utf-8 -*-
import os
import time
import getDeviceInfo

desPath="/Users/hanxiaochen/Desktop"
os.chdir(desPath)
while(1):

    print "----------------"
    print "请输入要执行的操作："
    print "1.卸载nr "
    print "2.清除nr数据"
    print  "3.截图"
    print "4.抓取log文件"
    print  "5.导出anr文件"
    print "6.获取手机信息"
    print "输入#结束"

    opt = input("请输入选项：")

    if(opt=='#'):
        break
    elif(opt==1):
        print "正在卸载nr..."
        os.system("adb shell uninstall com.mobilesrepublic.appy")
    elif(opt==2):
        print "清除nr数据.."
        os.system("adb shell pm clear com.mobilesrepublic.appy")
    elif(opt==3):
        print "截图中.."
        os.system("adb shell screencap -p /sdcard/sc.png")
        time.sleep(3)
        os.system("adb pull /sdcard/sc.png sc.png")
        print os.getcwd()
    elif(opt==4):
        os.system("adb logcat -d > log.txt")
        print os.getcwd()
    elif(opt==5):
        os.popen("adb pull data/anr/traces.txt traces.txt")
        print os.getcwd()
    elif(opt==6):
        getDeviceInfo.outPut()

