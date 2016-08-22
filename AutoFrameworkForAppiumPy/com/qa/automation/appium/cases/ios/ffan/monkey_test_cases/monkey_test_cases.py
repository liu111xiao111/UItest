#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import argparse
import datetime
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC

# 测试结果目录
reportPath = os.path.join(os.getcwd(), 'ios_monkey_log/')


class CrashError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MonkeyTestCases(TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        global reportPath
        self.reportPath = reportPath
        self.monkeyLogName = 'Ios_monkey.log'

    def test_case(self):
        self._monkeyTest()

        # monkey测试结果收集与统计
        monkeyLogFile = os.path.join(self.reportPath, self.monkeyLogName)
        crashNumber = 0
        f = open(monkeyLogFile)
        line = f.readline()
        while line:
            if line.find("crash report") != -1:
                crashNumber += 1
            line = f.readline()
        f.close()

        if crashNumber:
            raise CrashError('Monkey running failed with [[%s]] crash error.' % crashNumber)

    def _monkeyTest(self):
        monkeyLogFile = os.path.join(self.reportPath, self.monkeyLogName)
        command = "smart_monkey -a %s -w %s -d %s --drop-useless-img --detail-count 20 -t 16200 > %s" \
                  % (IDC.bundleId, IDC.udid, self.reportPath, monkeyLogFile)

        os.system(command)


def mkLogDir():
    '''
    创建日志结果目录, 判断当前位置是否存在测试结果目录, 如果存在, 则重命名原目录, 并新建测试结果目录
    '''
    if os.path.exists(reportPath):
        timestamp = os.path.getmtime(reportPath)
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d_%H_%M_%S')
        newDirName = 'ios_monkey_log_' + date

        newLogDir = os.path.join(os.path.dirname(os.path.dirname(reportPath)), newDirName)
        try:
            os.renames(os.path.dirname(reportPath), newLogDir)
        except Exception as e:
            raise IOError('Modify the [%s] directory name failed with following error: \n'
                          '%s' % (reportPath, e))

    try:
        os.makedirs(reportPath)
    except Exception as e:
        raise IOError('Create the [%s] directory failed with following error: \n'
                      '%s' % (reportPath, e))


def parse_command():
    '''
    解析日志路径命令行参数
    '''
    global reportPath
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_path', action='store', default='.',
                        dest='log_path', help='Setup log path, default is current execution directory.')
    args = parser.parse_args()
    logDir = os.path.abspath(args.log_path)
    reportPath = os.path.join(logDir, 'ios_monkey_log/')


if __name__ == "__main__":
    parse_command()
    mkLogDir()
    # HtmlTestRunner工具, 生成html测试结果报告
    suite = TestLoader().loadTestsFromTestCase(MonkeyTestCases)
    filename = os.path.join(reportPath, 'Feifan_ios_monkey_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_ios_monkey_test_report',
                                           description = 'Result for test')
    runner.run(suite)
