#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import pexpect
import argparse

import HTMLTestRunner
import unittest
#from unittest import TestCase
#from unittest.suite import TestSuite

from configs.driver_configs import appPackage_ffan
from cases.android.ffan.common.monkey_process import MonkeyHandle
from utility.monkeyMailProcess import sendTestResultMail
from cases.android.ffan.monkey_test_cases.gouWuZhongXin import GouWuZhongXinTestCase
#from cases.android.ffan.monkey_test_cases.meiShiHui import MeiShiHuiTestCase


class CrashError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MonkeyTestCases(unittest.TestCase):

    def test_case(self):
        '''
        unittest测试函数
        :return: None
        '''
        self._clearLogcat()

        self._monkeyTest()

        self._getLogcat()

        # monkey测试结果收集与统计
        monkeyLogFile = os.path.join(self.reportPath, self.monkeyLogName)
        crashNumber = 0
        f = open(monkeyLogFile, mode='r', encoding='utf-8')
        line = f.readline()
        while line:
            if line.find("// CRASH") != -1:
                crashNumber += 1
            line = f.readline()
        f.close()

        if crashNumber:
            raise CrashError('Monkey running failed with [[%s]] crash error.' % crashNumber)

    def _monkeyTest(self):
        '''
        monkey稳定性测试
        :return: None
        '''

        self._simiasqueoOption('True')
        # 执行monkey稳定性测试, 并生成测试结果日志文件
        monkeyLogFile = os.path.join('/sdcard', self.monkeyLogName)
        p = pexpect.spawn('adb shell')
        p.expect(r'^shell@', timeout=20)
        p.sendline('monkey -p %s --ignore-crashes --ignore-timeouts \
                --ignore-security-exceptions --throttle 300 --monitor-native-crashes \
                -v -v -v 200000 > %s &' %(appPackage_ffan, monkeyLogFile))
        p.expect(r'shell@', timeout=20)
        p.close()

        while True:
            time.sleep(5 * 60) # 每五分钟检查一次
            p = pexpect.spawn('adb shell')
            p.expect(r'^shell@', timeout=20)
            p.sendline('ps | grep monkey ')
            p.expect(r'shell@', timeout=20)
            context = p.before.decode('utf-8')
            if 'com.android.commands.monkey' in context:
                p.close()
                continue
            else:
                p.close()
                cmd = 'adb pull %s %s' % (monkeyLogFile, self.reportPath)
                os.system(cmd)
                break
        self._simiasqueoOption('False')

    def _clearLogcat(self):
        '''
        清理logcat缓存
        :return: None
        '''
        command = 'adb logcat -c'
        os.system(command)

    def _getLogcat(self):
        '''
        获取logcat输出结果
        :return: None
        '''
        logCatFile = os.path.join(self.reportPath, self.logcatLogName)
        command = "adb logcat -d > %s" % logCatFile
        os.system(command)

def parse_command():
    '''
    解析日志路径命令行参数
    '''
    global reportPath
    global sentMail
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_path', action='store', default='.',
                        dest='log_path', help='Setup log path, default is current execution directory.')
    parser.add_argument('-s', '--sent_mail', action='store_true', default=False, dest='sent_mail',
                        help='Sent mail.')
    args = parser.parse_args()
    logDir = os.path.abspath(args.log_path)
    sentMail = args.sent_mail
    reportPath = os.path.join(logDir, 'android_monkey_log/')


if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]

    # 飞凡数据存放路径
    reportPath = "%s/report/stability/%s/%s" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportPath):
        os.makedirs(reportPath)

    startTime = time.strftime('%Y/%m/%d %H:%M:%S')

    try:
#         startTraffic, sTime = perf.getTraffic()
#         command = 'adb logcat -c'
#         os.system(command)

        # 添加测试用例
#         suite = unittest.TestSuite()
#         suite.addTest(GouWuZhongXinTestCase("testGouWuZhongXin")) # 电影 No.06
#         #suite.addTest(MeiShiHuiTestCase("testMeiShiHui")) # 电影 No.06
# 
#         runner = unittest.TextTestRunner()
        executeTimes = reportPath + "/executeTimes.txt"
        for i in range(1):
            f = open(executeTimes, "w")
            f.write(str(i+1))
            f.close()
            # 添加测试用例
            suite = unittest.TestSuite()
            suite.addTest(GouWuZhongXinTestCase("testGouWuZhongXin")) # 电影 No.06
            #suite.addTest(MeiShiHuiTestCase("testMeiShiHui")) # 电影 No.06

            runner = unittest.TextTestRunner()
            runner.run(suite)

        if os.path.exists(executeTimes):
            os.remove(executeTimes)

#         filename = os.path.join(reportpath, 'feifan_automation_test_report.html')
#         fp = open(filename, 'wb')
#         runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
#                                            description='Result for test')

        # monkey测试结果收集与统计
#         monkeyLogFile = os.path.join(self.reportPath, self.monkeyLogName)
#         crashNumber = 0
#         f = open(monkeyLogFile, mode='r', encoding='utf-8')
#         line = f.readline()
#         while line:
#             if line.find("// CRASH") != -1:
#                 crashNumber += 1
#             line = f.readline()
#         f.close()
# 
#         if crashNumber:
#             raise CrashError('Monkey running failed with [[%s]] crash error.' % crashNumber)

    except CrashError as e:
        raise CrashError(e)
    finally:
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
#         endTraffic, eTime = perf.getTraffic()
#         perf.parseTraffic(startTraffic, endTraffic, round(eTime-sTime))
#         MonkeyHandle().Handle(startTime, endTime, reportPath)
        MonkeyHandle().monkeyHandleForStability(startTime, endTime, reportPath)
#         if sentMail:
#             sendTestResultMail(startTime, endTime, reportPath, 'android')
