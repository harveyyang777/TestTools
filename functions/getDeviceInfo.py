# -*- coding:utf-8 -*-
import os

def outPut():
    print "手机信息如下,请稍后..."
    version = os.popen("adb shell getprop ro.build.version.release").readline().rstrip()
    model = os.popen("adb shell getprop ro.product.model").readline().rstrip()
    wmsize = os.popen("adb shell wm size").readline().rstrip()
    density = os.popen("adb shell wm density").readline().rstrip()
    aid = os.popen("adb shell settings get secure android_id").readline().rstrip()
    brand = os.popen("adb shell getprop ro.product.brand").readline().rstrip()

    print "系统版本：" + version
    print "品牌：" + brand
    print "型号：" + model
    print "屏幕分辨率：" + wmsize
    print "屏幕密度：" + density
    print "aid:" + aid


