# -*- coding: utf-8 -*-
'''
Created on Aug 31, 2016

@author: songbo
'''

import os
import time
from subprocess import Popen, PIPE

from configs.driver_configs import appPackage_ffan


class Performance(object):
    def __init__(self, reportPath):
        '''
        初始化性能测试信息
        :param reportPath: 日志文件保存路径
        '''
        self.reportPath = reportPath
        self.now = time.strftime("%Y_%m_%d_%H_%M_%S")

    def getPid(self):
        '''
        获取应用PID
        :return: 应用PID
        '''
        cmdPid = "adb shell ps | grep ' %s\r' | awk '{print $2}'" % (appPackage_ffan)
        ret = Popen(cmdPid, shell=True, stdout=PIPE, stderr=PIPE)

        pid, err = ret.communicate()

        return pid.decode('utf-8').split('\n')[0]

    def getCpu(self):
        '''
        获取应用cpu使用状态, 并保存至日志文件中
        :return: 无
        '''
        pid = self.getPid()
        if pid:
            cpu = "dumpsys cpuinfo | grep " + pid
            cmdCpu = "adb shell \"%s\"" % (cpu)
            ret = Popen(cmdCpu, shell=True, stdout=PIPE, stderr=PIPE)

            cpuInfo, err = ret.communicate()

            if err or not cpuInfo:
                return
            cpuRate = cpuInfo.decode('utf-8').split("/" + appPackage_ffan + ":")[0].split("%")[0]
            logName = "Cpu_performance.txt"
            logPath = os.path.join(self.reportPath, logName)
            f = open(logPath, "a")
            if len(cpuRate.strip().split(' ')) == 1:
                f.write("%s:%s" % (time.strftime("%Y/%m/%d %H_%M_%S"), cpuRate) + "\n")
            f.close()

    def getMemory(self):
        '''
        获取应用内存使用状态, 并保存至日志文件中
        :return: 无
        '''
        pss = "dumpsys meminfo " + appPackage_ffan + " | grep TOTAL"
        cmdPss = "adb shell \"%s\"" % (pss)
        ret = Popen(cmdPss, shell=True, stdout=PIPE, stderr=PIPE)

        memInfo, err = ret.communicate()

        if err or not memInfo:
            return
        mem = int(memInfo.decode('utf-8').split("   ")[3])/1024
        logName = "Mem_peformance.txt"
        logPath = os.path.join(self.reportPath, logName)
        f = open(logPath, "a")
        f.write("%s:%s" % (time.strftime("%Y/%m/%d %H_%M_%S"), mem) + "\n")
        f.close()

    def getTraffic(self):
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

        getTime = time.time()

        return totalTraffic, getTime

    def parseTraffic(self, startTraffic, endTraffic, duration):
        traffic = round((endTraffic - startTraffic) / 1024 / 1024, 2)

        logName = "Traffic_performance.txt"
        logPath = os.path.join(self.reportPath, logName)
        f = open(logPath, "a")
        f.write("%s:%s" % (duration, traffic) + "\n")
        f.close()

    def getRx(self):
        '''
        获取应用下行速率
        :return: 无
        '''
        currentRx = self._getRate('down')
        if currentRx is None:
            return

        logName = "Rx_performance.txt"
        logPath = os.path.join(self.reportPath, logName)
        f = open(logPath, "a")
        f.write("%s:%s" % (time.strftime("%Y/%m/%d %H_%M_%S"), currentRx) + "\n")
        f.close()

    def getTx(self):
        '''
        获取应用上行速率
        :return: 无
        '''
        currentTx = self._getRate('up')
        if currentTx is None:
            return

        logName = "Tx_performance.txt"
        logPath = os.path.join(self.reportPath, logName)
        f = open(logPath, "a")
        f.write("%s:%s" % (time.strftime("%Y/%m/%d %H_%M_%S"), currentTx) + "\n")
        f.close()

    def _getRate(self, sort):
        '''
        获取上下行速率
        :return: 速率
        '''
        pid = self.getPid()
        uid = self._getUid(pid)
        currentRateList = []
        for _ in range(2):
            cmdRate = "adb shell cat /proc/net/xt_qtaguid/stats | grep %s" % uid
            ret = Popen(cmdRate, shell=True, stdout=PIPE, stderr=PIPE)

            rateInfo, err = ret.communicate()
            if err or not rateInfo:
                return
            rateLines = rateInfo.decode('utf-8').split('\n')
            totlaRate = 0
            for rateLine in rateLines:
                try:
                    if sort == 'up':
                        rate = float(rateLine.split(' ')[7])
                    elif sort == 'down':
                        rate = float(rateLine.split(' ')[5])
                    else:
                        return None
                except:
                    break
                totlaRate = rate + totlaRate
            currentRateList.append(totlaRate)
            time.sleep(1)

        currentRate = round((currentRateList[1] - currentRateList[0]) / 1024, 2)
        if currentRate < 0:
            return 0
        else:
            return currentRate

    def _getUid(self, pid):
        '''
        获取进程UID
        :param pid: 进程PID
        :return: 进程UID
        '''
        cmdUid = "adb shell cat /proc/%s/status | grep Uid:" % pid
        ret = Popen(cmdUid, shell=True, stdout=PIPE, stderr=PIPE)

        uidInfo, err = ret.communicate()
        if err or not uidInfo:
            return

        uid = uidInfo.decode('utf-8').split('\t')[1]
        return uid

Performance('/Users/songbo/').getCpu()