#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC


class MonkeyTestCases(TestCase):

    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_case(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        nowTime = time.strftime('%Y%m%d%H%M%S')
        command = "instruments -w %s -t %sAutomation.tracetemplate com.dianshang.wanhui \
                    -e UIASCRIPT %sUIAutoMonkey.js > IOS_MonkeyTest_%s.log" \
                    % (IDC.udid, resourcesDirectory, resourcesDirectory, nowTime)
        os.system(command)
        f = open("IOS_MonkeyTest_%s.log" % (nowTime))
        line = f.readline()
        while line:
            if line.find("Instruments Trace Complete") != -1:
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
