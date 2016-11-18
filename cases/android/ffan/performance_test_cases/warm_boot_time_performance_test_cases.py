# -*- coding: utf-8 -*-

import os
import time
import subprocess


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class WarmBootTimePerformanceTestCases():
    '''
    作者 刘涛
    热启动时间情况性能测试
    '''

    def getWarmBootTime(self, reportPath, pkName, actiName):
        bootTime = "am start -W " + pkName + "/" + actiName + " | grep TotalTime"
        cmdam = "adb shell \"%s\"" % bootTime
        keycode = "keyevent KEYCODE_BACK"
        cmdBack = "adb shell input %s" % keycode
        file = os.path.join(reportPath, "boottime.txt")
        f1 = open(file, mode="a", encoding='utf-8')
        os.system('adb shell "am start -W "' + pkName + '/' + actiName )
        for _ in range(0,2):
            os.system(cmdBack)
            time.sleep(0.3)
            os.system(cmdBack)
            time.sleep(0.3)
            os.system(cmdBack)
            time.sleep(10)
            pipe = subprocess.Popen(cmdam, shell=True, stdout = f1)
            pipe.stdout
            time.sleep(5)
        os.system(cmdBack)
        time.sleep(0.3)
        os.system(cmdBack)
        time.sleep(0.3)
        os.system(cmdBack)
        f1.close()
