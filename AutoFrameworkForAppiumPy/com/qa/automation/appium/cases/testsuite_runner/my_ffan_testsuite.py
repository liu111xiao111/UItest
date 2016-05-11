# -*- coding: utf-8 -*-

import sys,os
# reload(sys)
# sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


from com.qa.automation.appium.cases.ffan.myffan_cases import *

import unittest
import HTMLTestRunner

build_num=sys.argv[1]

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))
reportpath = "%s/report/ffan/%s/%s/" % (root_dir,time.strftime("%Y%m%d"),build_num)
# root_dir/ffan/date/build_num
if not os.path.exists(reportpath):
    os.makedirs(reportpath)


suite = unittest.TestLoader().loadTestsFromTestCase(MyFfanCases)
now = time.strftime('%H_%M_%S')

filename = reportpath + 'feifan_automation_test_report_' + now + '.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                       description='Result for test')
runner.run(suite)