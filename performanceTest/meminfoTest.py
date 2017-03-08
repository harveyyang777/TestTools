# -*- coding:utf-8 -*-
import os
import re
import time

#执行次数
for j in range(5):

    #间隔时间（s）
    time.sleep(10)
    meminfo = os.popen("adb shell dumpsys meminfo com.mobilesrepublic.appy").readlines()


    for i in range(len(meminfo)):
        mem=meminfo[i].lstrip()
     #   print mem
        m=re.match("TOTAL",mem) ##通过关键字定位筛选

        if m:
            mem=mem.split("   ")
          #  print mem
            count=int(mem[1])/1024
            print count
            break

