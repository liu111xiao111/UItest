#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import pexpect
import argparse
import datetime
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.configs.driver_configs import appPackage_ffan

# 测试结果目录
reportPath = os.path.join(os.getcwd(), 'android_monkey_log/')


class CrashError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MonkeyTestCases(TestCase):
    def tearDown(self):
        '''
        unittest资源释放回滚函数, 关闭测试应用
        :return: None
        '''
        command = '%sadb shell am force-stop %s' % (self.resourcesDirectory, appPackage_ffan)
        os.system(command)

    def setUp(self):
        '''
        unittest初始化函数
        :return: None
        '''
        self.monkeyLogName = 'Android_monkey.log'
        self.logcatLogName = 'Android_monkey_logcat.log'
        self.reportPath = reportPath
        self.resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"

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
        f = open(monkeyLogFile)
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

        # 执行monkey稳定性测试, 并生成测试结果日志文件
        monkeyLogFile = os.path.join('/sdcard', self.monkeyLogName)
        p = pexpect.spawn('%sadb shell' % self.resourcesDirectory)
        p.expect(r'^shell@', timeout=20)
        p.sendline('monkey -p %s --ignore-crashes --ignore-timeouts \
                --ignore-security-exceptions --pct-touch 90 --pct-motion 4 \
                --throttle 300 --monitor-native-crashes -v -v -v 130000 > %s &' %(appPackage_ffan, monkeyLogFile))
        p.expect(r'shell@', timeout=20)
        p.close()

        time.sleep(4 * 60 * 60) # 睡眠等待4小时
        while True:
            time.sleep(5 * 60) # 每五分钟检查一次
            p = pexpect.spawn('%sadb shell' % self.resourcesDirectory)
            p.expect(r'^shell@', timeout=20)
            p.sendline('ps | grep monkey ')
            p.expect(r'shell@', timeout=20)
            context = p.before.decode('utf-8')
            if 'com.android.commands.monkey' in context:
                p.close()
                continue
            else:
                p.close()
                cmd = '%sadb pull %s %s' % (self.resourcesDirectory, monkeyLogFile, self.reportPath)
                os.system(cmd)
                break

    def _clearLogcat(self):
        '''
        清理logcat缓存
        :return: None
        '''
        command = '%sadb logcat -c' % self.resourcesDirectory
        os.system(command)

    def _getLogcat(self):
        '''
        获取logcat输出结果
        :return: None
        '''
        logCatFile = os.path.join(self.reportPath, self.logcatLogName)
        command = "%sadb logcat -d > %s" % (self.resourcesDirectory, logCatFile)
        os.system(command)


def mkLogDir():
    '''
    创建日志结果目录, 判断当前位置是否存在测试结果目录, 如果存在, 则重命名原目录, 并新建测试结果目录
    '''
    if os.path.exists(reportPath):
        timestamp = os.path.getmtime(reportPath)
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d_%H_%M_%S')
        newDirName = 'android_monkey_log_' + date

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
    reportPath = os.path.join(logDir, 'android_monkey_log/')


if __name__ == "__main__":
    parse_command()
    mkLogDir()

    # HtmlTestRunner工具, 生成html测试结果报告
    suite = TestLoader().loadTestsFromTestCase(MonkeyTestCases)
    filename = os.path.join(reportPath, 'Feifan_android_monkey_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_android_monkey_test_report',
                                           description='Result for test')
    runner.run(suite)
