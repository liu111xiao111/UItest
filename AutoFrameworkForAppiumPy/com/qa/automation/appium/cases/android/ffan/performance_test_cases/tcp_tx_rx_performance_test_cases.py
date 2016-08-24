import os
import re
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan

uidFile = "getUid.txt"
tcpSndFile = "getTcpSnd.txt"
tcpRevFile = "getTcpRev.txt"
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class TcpTxRxPerformanceTestCases(TestCase):
    '''
    作者 刘涛
    CPU使用情况性能测试
    '''

    def getPid(self):
        now = time.strftime('%Y%m%d%H%M%S')
        pidFile = "pid_" + now + ".txt"
        cmdpid = "%sadb shell ps | grep %s | awk '{print $2}' | head -n 1 > %s" % (resourcesDirectory, appPackage_ffan, pidFile)
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
            if uid != 0:
                f2 = open(tcpSndFile, "a")
                f2.write("cd /proc/uid_stat/" + uid + "\n")
                f2.write("cat tcp_snd\n")
                f2.write("exit\n")
                f2.close()
                f3 = open(tcpRevFile, "a")
                f3.write("cd /proc/uid_stat/" + uid + "\n")
                f3.write("cat tcp_rcv\n")
                f3.write("exit\n")
                f3.close()
                break
        if os.path.exists(logFile):
            os.remove(logFile)
        #print("UID: " + uid)

    def getTcpTxRx(self):

        print("Start Net Up Flow & Down Flow Test, please run the app and keep operation until the Test complete")
        now = time.strftime('%Y%m%d%H%M%S')
        tcpTransmitData = "TCP_TX_RX_" + appPackage_ffan + "_" + now + ".txt"
        for _ in range(5):
            self.getUid()
            nowTest = time.strftime('%Y%m%d%H%M%S')
            logFile = "cmd_tcp_send_data" + nowTest + ".txt"
            f = open(logFile, "a")
            tcpSnd = "%sadb shell < %s > %s" % (resourcesDirectory, tcpSndFile, logFile)
            pipe = subprocess.Popen(tcpSnd, shell=True, stdout = f)
            pipe.stdout
            os.system(tcpSnd)
            f.close()

            logName = "cmd_tcp_receive_data" + nowTest + ".txt"
            ff = open(logName, "a")
            tcpRev = "%sadb shell < %s > %s" % (resourcesDirectory, tcpRevFile, logName)
            pipe = subprocess.Popen(tcpSnd, shell=True, stdout = ff)
            pipe.stdout
            os.system(tcpRev)
            ff.close()
    
            f1 = open(logFile,"r")
            lines = f1.readlines()
            f1.close()
            tx = 0
            for line in lines:
                m = re.match(r'^[0-9]', line)
                if m:
                    tx = line
                    break

            f3 = open(logName,"r")
            linesRev = f3.readlines()
            f3.close()
            rx = 0
            for lineRev in linesRev:
                n = re.match(r'^[0-9]', lineRev)
                if n:
                    rx = lineRev
                    break

            f2 = open(tcpTransmitData,"a")
            f2.write("TCP_TX: " + str(tx))
            if str(tx) == '0':
                f2.write("\n")
            f2.write("TCP_RX: " + str(rx))
            f2.write("\n")
            f2.close()
            if os.path.exists(logFile):
                os.remove(logFile)
            if os.path.exists(logName):
                os.remove(logName)

            if os.path.exists(tcpSndFile):
                os.remove(tcpSndFile)
            if os.path.exists(tcpRevFile):
                os.remove(tcpRevFile)

            print("\nNet Up Flow: " + str(tx))
            print("Net Down Flow: " + str(rx))
            if str(tx) == '0':
                print("\n")
            time.sleep(2)
        print("Net Up Flow & Down Flow Test complete, go to " + tcpTransmitData + " and see the details")
