# -*- coding: utf-8 -*-

import os
import time
import subprocess
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import appActivity_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class WarmBootTimePerformanceTestCases():
    '''
    作者 刘涛
    热启动时间情况性能测试
    '''

    def getWarmBootTime(self, reportPath):
        bootTime = "am start -W " + appPackage_ffan + "/" + appActivity_ffan + " | grep TotalTime"
        cmdam = "adb shell \"%s\"" % bootTime
        keycode = "keyevent KEYCODE_BACK"
        cmdBack = "adb shell input %s" % keycode
        file = os.path.join(reportPath, "WarmBootTime_performance.txt")
        f1 = open(file, mode="a", encoding='utf-8')
        os.system('adb shell "am start -W "' + appPackage_ffan + '/' + appActivity_ffan )
        for _ in range(0,10):
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
