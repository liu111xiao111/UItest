#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan


class MonkeyTestCases(TestCase):

    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_case(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        nowTime = time.strftime('%Y%m%d%H%M%S')
        command = "%sadb shell monkey -p %s --ignore-crashes --ignore-timeouts \
                    --ignore-security-exceptions --pct-touch 90 --pct-motion 4 \
                    --throttle 300 --monitor-native-crashes -v -v -v 220000 > Android_MonkeyTest_%s.log" \
                    % (resourcesDirectory, appPackage_ffan, nowTime)
        os.system(command)
        f = open("Android_MonkeyTest_%s.log" % (nowTime))
        line = f.readline()
        while line:
            if (line.find(":Sending rotation") != -1) or \
                (line.find(":Dropped:") != -1) or \
                (line.find("## Network") != -1) or \
                (line.find("// Monkey finished") != -1):
                print(line)
            line = f.readline()
        f.close()  


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MonkeyTestCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
