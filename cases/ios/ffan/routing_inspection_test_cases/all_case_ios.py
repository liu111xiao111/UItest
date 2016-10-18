# -*- coding:utf-8 -*-

import sys, os
import time
from unittest.suite import TestSuite

import HTMLTestRunner

from utility.mailProcess import sendTestResultMail
from cases.ios.ffan.common.reportProcess import ReportHandle


if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    # suite.addTest(ActivitySharingCases("test_case"))

    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'feifan_automation_test_report_ios.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)

    if sentMail:
        sendTestResultMail(reportpath, 'ios')
