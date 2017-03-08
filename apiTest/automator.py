# -*- coding:utf-8 -*-

import os
import time
os.popen("adb shell am start -W -n com.mobilesrepublic.appy/.InitActviity ")
time.sleep(5)
print os.popen("adb shell am start -W -n com.mobilesrepublic.appy/com.cmcm.newsindia.MainActivity ").readline()

