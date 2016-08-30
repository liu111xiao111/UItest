import os
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class WarmBootTimePerformanceTestCases(TestCase):
    '''
    作者 刘涛
    热启动时间情况性能测试
    '''

    def getWarmBootTime(self):
        print("Start the WarmBoot test, please open the file until test complete")
        bootTime = "am start -W " + appPackage_ffan + "/" + appActivity_ffan + " | grep TotalTime"
        cmdam = "%sadb shell \"%s\"" % (resourcesDirectory, bootTime)
        keycode = "keyevent KEYCODE_BACK"
        cmdBack = "%sadb shell input %s" % (resourcesDirectory, keycode)
        f1 = open("WarmBootTime_" + appPackage_ffan + "_" + now + ".txt", "a")
        for _ in range(0,10):
            os.system(cmdBack)
            time.sleep(0.3)
            os.system(cmdBack)
            time.sleep(10)
            pipe = subprocess.Popen(cmdam, shell=True, stdout = f1)
            pipe.stdout
            time.sleep(5)
        f1.close()
        f2 = open("WarmBootTime_" + appPackage_ffan + "_" + now + ".txt", "r")
        allTime = []
        originals = f2.readlines()
        f2.close
        for contents in originals:
            try:
                total = contents.split(" ")[1]
                allTime.append(total)
                time.sleep(1)
            except:
                continue
        finalTime = 0
        for i in range (len(allTime)):
            finalTime = int (allTime[i]) + finalTime
            time.sleep(1)
        averageTime = finalTime/10
        logName = "WarmBootTime_" + appPackage_ffan + "_" + now + ".txt"
        f = open(logName, "a")
        f.write("\nTotal Time: " + str(finalTime) + "\n")
        f.write("Average Time: " + str(averageTime))
        time.sleep(1)
        f.close
        print("getWarmBootTime Test complete, go to " + logName + " and see the details\n")
