# -*- coding: utf-8 -*-

import os
import time
import subprocess
from unittest import TestCase
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import appActivity_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class ColdBootTimePerformanceTestCases(TestCase):
    '''
    作者 刘涛
    冷启动时间情况性能测试
    '''

    def getColdBootTime(self, reportPath):
        bootTime = "am start -W " + appPackage_ffan + "/" + appActivity_ffan + " | grep TotalTime"
        cmdam = "adb shell \"%s\"" % bootTime
        kill = "am force-stop " + appPackage_ffan
        cmdKill = "adb shell \"%s\"" % kill
        file = os.path.join(reportPath, "ColdBootTime_performance.txt")
        f1 = open(file, mode="a", encoding='utf-8')
        for _ in range(0,10):
            os.system(cmdKill)
            time.sleep(10)
            pipe = subprocess.Popen(cmdam, shell=True, stdout = f1)
            pipe.stdout
            time.sleep(10)
        f1.close()
        # f2 = open("ColdBootTime_performance.txt", "r")
        # allTime = []
        # originals = f2.readlines()
        # f2.close
        # for contents in originals:
        #     try:
        #         total = contents.split(" ")[1]
        #         allTime.append(total)
        #         time.sleep(1)
        #     except:
        #         continue
        # finalTime = 0
        # for i in range (len(allTime)):
        #     finalTime = int (allTime[i]) + finalTime
        #     time.sleep(1)
        # averageTime = finalTime/10
        # logName = "ColdBootTime_" + appPackage_ffan + "_" + now + ".txt"
        # f = open(logName, "a")
        # f.write("\nTotal Time: " + str(finalTime) + "\n")
        # f.write("Average Time: " + str(averageTime))
        # time.sleep(1)
        # f.close
        # print("getColdBootTime Test complete, go to " + logName + " and see the details\n")
