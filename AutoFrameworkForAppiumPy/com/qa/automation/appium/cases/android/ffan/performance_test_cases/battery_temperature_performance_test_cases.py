import os
import re
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class BatteryTemperaturePerformanceTestCases(TestCase):
    '''
    作者 刘涛
    电池温度情况性能测试
    '''

    def getBatteryTemperature(self):

        print("Start the Battery Temperature test, please run the app and keep operation until the Test complete")
        logFile = "TEMP_" + appPackage_ffan + "_" + now + ".txt"
        cmdBtyTmpt = "%sadb shell dumpsys battery" % (resourcesDirectory)
        #print(cmdpss)
        cmdFile = "battery_temperature_" + appPackage_ffan + "_" + now + ".txt"
        f1 = open(cmdFile, "a")
        for _ in range(0, 2):
            pipe = subprocess.Popen(cmdBtyTmpt, shell=True, stdout = f1)
            pipe.stdout
            time.sleep(60)
        f1.close()
        f2 = open(cmdFile, "r")
        originals = f2.readlines()
        f2.close
        f3 = open(logFile, "a")
        f3.write("Below is the Battery Temperature:" + '\n')
        for contents in originals:
            try:
                print(contents)
                if "temperature:" in contents:
                    tmp = contents.split(" ")[3]
                    temp = float(re.findall(r'[0-9]+.[0-9]+', tmp)[0])
                    temperature = round(temp/10, 2)
                    f3.write("temperature: " + str(temperature) + "\n")
            except:
                continue
        f3.close()
        time.sleep(1)
        if os.path.exists(cmdFile):
            os.remove(cmdFile)
        print("getBatteryTemperature Test complete, go to " + logFile + " and see the details\n")
