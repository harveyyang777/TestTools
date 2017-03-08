import os
import time

os.popen("adb logcat -c")
os.popen("adb shell am force-stop com.mobilesrepublic.appy")
time.sleep(2)
os.popen("adb shell am -n com.mobilesrepublic.appy/com.cmcm.newsindia.MainActivity")
time.sleep(2)
os.popen("adb shell am start -n com.mobilesrepublic.appy/com.cmcm.onews.ui.NewsActivity")
time.sleep(1)
os.popen("adb shell input tap 151 1674")
time.sleep(2)
os.popen("adb shell input tap 250 900")
time.sleep(1)
os.getcwd()
os.popen("adb logcat -d -s ActivityManager |grep 'START\|Display' >log.txt")
