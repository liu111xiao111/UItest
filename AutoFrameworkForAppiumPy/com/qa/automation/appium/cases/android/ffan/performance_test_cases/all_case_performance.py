# -*- coding:utf-8 -*-

import sys,os

import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner
from unittest.suite import TestSuite
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases


if __name__ == "__main__":
    build_num = sys.argv[1]

    #root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_performance/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    suite.addTest(ColdBootTimePerformanceTestCases("getColdBootTime"))
    suite.addTest(WarmBootTimePerformanceTestCases("getWarmBootTime"))


    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'feifan_automation_test_report_perf.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_perf',
                                           description='Result for test')
    runner.run(suite)
