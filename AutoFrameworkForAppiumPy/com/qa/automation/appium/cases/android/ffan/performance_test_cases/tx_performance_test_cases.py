import os
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan

uidFile = "getUid.txt"
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class TxPerformanceTestCases(TestCase):
    '''
    作者 刘涛
    CPU使用情况性能测试
    '''

    def getPid(self):
        now = time.strftime('%Y%m%d%H%M%S')
        pidFile = "pid_" + now + ".txt"
        cmdpid = "%sadb shell ps | grep ' %s\r' | awk '{print $2}' > %s" % (resourcesDirectory, appPackage_ffan, pidFile)
        os.system(cmdpid)
        f = open(pidFile)
        pid = f.readline()
        if os.path.exists(pidFile):
            os.remove(pidFile)
        f = open(uidFile, "a")
        f.write("cd /proc/" + pid)
        f.write("cat status\n")
        f.write("exit\n")
        f.close()
        #print("PID: "+ pid)

    def getUid(self):
        global uidFile
        self.getPid()
        time.sleep(2)
        now = time.strftime('%Y%m%d%H%M%S')
        logFile = "uid_" + appPackage_ffan + now + ".txt"
        f = open(logFile, "a")
        cmdUid = "%sadb shell < %s > %s" % (resourcesDirectory, uidFile, logFile)
        pipe = subprocess.Popen(cmdUid, shell=True, stdout = f)
        pipe.stdout
        os.system(cmdUid)
        f.close()
        if os.path.exists(uidFile):
            os.remove(uidFile)

        f1 = open(logFile,"r")
        lines = f1.readlines()
        f1.close()
        uid = 0
        for line in lines:
            if "Uid:" in line:
                uid = line.split("\t")[1]
                break
        if os.path.exists(logFile):
            os.remove(logFile)
        #print("UID: " + uid)
        return uid

    def getTxBytes(self):

        print("Start Up Flow Test, please run the app and keep operation until the Test complete")
        now = time.strftime('%Y%m%d%H%M%S')
        transmitData = "TX_" + appPackage_ffan + "_" + now + ".txt"
        f2 = open(transmitData,"a")
        f2.write("Below is Net Down Flow:\n")
        f2.close()
        for _ in range(5):
            currentTxList = []
            for i in range(2):
                uid = self.getUid()
                num = str(i + 1)
                tmpLog = "cmd_" + appPackage_ffan + "_" + num + ".txt"
                f = open(tmpLog,"a")
                cmdTx = "%sadb shell cat /proc/net/xt_qtaguid/stats | grep %s" % (resourcesDirectory, uid)
                pipe = subprocess.Popen(cmdTx, shell=True, stdout = f)
                pipe.stdout
                f.close()
                time.sleep(1)

                f1 = open(tmpLog,"r")
                lines = f1.readlines()
                f1.close()
                totalTx = 0

                for line in lines:
                    tx = float(line.split(" ")[7])
                    totalTx = tx + totalTx
                currentTxList.append(totalTx)

                if os.path.exists(tmpLog):
                    os.remove(tmpLog)

            currentTx = round((currentTxList[1] - currentTxList[0]) / 1024, 2)
            f2 = open(transmitData,"a")
            f2.write("TX: " + str(currentTx) + "KB\n")
            f2.close()

            print("\nNet Up Flow: " + str(currentTx) + "KB\n")
            time.sleep(1)
        print("Net Up Flow Test complete, go to " + transmitData + " and see the details\n")
