# -*- coding: utf-8 -*-


import os
import time
from subprocess import Popen, PIPE


class TestMethod():


    def getTraffic(self):
        print("get traffic")
        cmdTraffic = "adb shell cat /proc/net/xt_qtaguid/stats | grep rmnet0"
        ret = Popen(cmdTraffic, shell=True, stdout=PIPE, stderr=PIPE)
        trafficInfo, err = ret.communicate()
        if err or not trafficInfo:
            cmdTraffic = "adb shell cat /proc/net/xt_qtaguid/stats | grep wlan0"
            ret = Popen(cmdTraffic, shell=True, stdout=PIPE, stderr=PIPE)
            trafficInfo, err = ret.communicate()
            if err or not trafficInfo:
                return
        rateLines = trafficInfo.decode('utf-8').split('\n')
        totalTraffic = 0
        for rateLine in rateLines:
            try:
                upTraffic = float(rateLine.split(' ')[7])
                downTraffic = float(rateLine.split(' ')[5])
            except:
                break
            totalTraffic = upTraffic + downTraffic + totalTraffic

        if totalTraffic is None:
            totalTraffic = "Get traffic failed"

        getTime = time.time()

        print(totalTraffic)

        return totalTraffic, getTime

if __name__ == "__main__":
    testMethod = TestMethod()
    traffic , time = testMethod.getTraffic()
