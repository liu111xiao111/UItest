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
        os.system(cmdKill)
        f1.close()
