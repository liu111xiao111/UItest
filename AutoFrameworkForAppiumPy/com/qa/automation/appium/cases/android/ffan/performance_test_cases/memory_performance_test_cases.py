import os
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class MemoryPerformanceTestCases(TestCase):
    '''
    作者 刘涛
    Memory使用情况性能测试
    '''

    def getMemory(self):

        print("Start the Memory test, please run the app and keep operation until the Test complete")
        pss = "dumpsys meminfo " + appPackage_ffan + " | grep TOTAL"
        cmdpss = "%sadb shell \"%s\"" % (resourcesDirectory, pss)
        #print(cmdpss)
        f1 = open("PSS_" + appPackage_ffan + "_" + now + ".txt", "a")
        for _ in range(0, 120):
            pipe = subprocess.Popen(cmdpss, shell=True, stdout = f1)
            pipe.stdout
            time.sleep(1)
        f1.close()
        f2 = open("PSS_" + appPackage_ffan + "_" + now + ".txt", "r")
        totalHeapSize = []
        originals = f2.readlines()
        f2.close
        for contents in originals:
            try:
                total = contents.split("   ")[3]
                totalHeapSize.append(total)
            except:
                continue
        logName = "PSS_" + appPackage_ffan + "_" + now + ".txt"
        f = open(logName, "a")
        f.write("Below is the memory(pss):" + '\n')
        for i in range (len(totalHeapSize)):
            m = int(totalHeapSize[i])/1024
            f.write(str(m) + '\n')
            #f.write(totalHeapSize[i] + '\n')
            time.sleep(1)
            f.close
        print("getMemory Test complete, go to " + logName + " and see the details\n")
