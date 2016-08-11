#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import argparse
import datetime
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.configs.driver_configs import appPackage_ffan

reportpath = os.getcwd()
logDir = os.path.join(reportpath, 'android_monkey_log')


class CrashError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class MonkeyTestCases(TestCase):
    def tearDown(self):
        command = '%sadb shell am force-stop %s' % (self.resourcesDirectory, appPackage_ffan)
        os.system(command)

    def setUp(self):
        global logDir
        self.monkeyLogName = 'Android_monkey.log'
        self.logcatLogName = 'Android_monkey_logcat.log'
        self.logDir = logDir
        self.resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"

    def test_case(self):
        self._clearLogcat()

        self._monkeyTest()

        self._getLogcat()
        monkeyLogFile = os.path.join(self.logDir, self.monkeyLogName)
        f = open(monkeyLogFile)
        line = f.readline()
        while line:
            if line.find("// CRASH") != -1:
                raise CrashError('Monkey running failed with crash error.')
            line = f.readline()
        f.close()

    def _monkeyTest(self):
        monkeyLogFile = os.path.join(self.logDir, self.monkeyLogName)
        command = "%sadb shell monkey -p %s --ignore-crashes --ignore-timeouts \
                    --ignore-security-exceptions --pct-touch 90 --pct-motion 4 \
                    --throttle 300 --monitor-native-crashes -v -v -v 200000 > %s" \
                    % (self.resourcesDirectory, appPackage_ffan, monkeyLogFile)
        os.system(command)

    def _clearLogcat(self):
        command = '%sadb logcat -c' % self.resourcesDirectory
        os.system(command)

    def _getLogcat(self):
        logCatFile = os.path.join(self.logDir, self.logcatLogName)
        command = "%sadb logcat -d > %s" \
                    % (self.resourcesDirectory, logCatFile)
        os.system(command)

def mkLogDir():
    global logDir, reportpath
    if os.path.exists(logDir):
        timestamp = os.path.getmtime(logDir)
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d_%H_%M_%S')
        newDirName = 'android_monkey_log_' + date
        newLogDir = os.path.join(reportpath, newDirName)
        try:
            os.renames(logDir, newLogDir)
        except Exception as e:
            raise IOError('Modify the [%s] directory name failed with following error: \n'
                          '%s' % (logDir, e))

    try:
        os.makedirs(logDir)
    except Exception as e:
        raise IOError('Create the [%s] directory failed with following error: \n'
                      '%s' % (logDir, e))

def parse_command():
    global reportpath
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_path', action='store', default='.',
                        dest='log_path', help='Setup log path, default is current execution directory.')
    args = parser.parse_args()
    reportpath = args.log_path

if __name__ == "__main__":
    parse_command()
    mkLogDir()
    suite = TestLoader().loadTestsFromTestCase(MonkeyTestCases)
    filename = os.path.join(logDir, 'Feifan_android_monkey_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_android_monkey_test_report',
                                           description='Result for test')
    runner.run(suite)
