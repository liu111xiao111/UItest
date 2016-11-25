# -*- coding:utf-8 -*-

import sys, os
import time
from unittest import TestCase
from unittest import TestLoader
from unittest.suite import TestSuite

import HTMLTestRunner

from cases.ios.ffan.common.reportProcess import ReportHandle
from cases.ios.ffan.routing_inspection_test_cases.gouWuZhongXin import GouWuZhongXinTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMaiDan import GuangChangMaiDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMeiShiHui import GuangChangMeiShiHuiTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangSouSuo import GuangChangSouSuoTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangTingChe import GuangChangTingCheTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangZhaoDian import GuangChangZhaoDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.paiDuiQuHao import PaiDuiQuHaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoMenDian import QuanChengSouSuoMenDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoPinPai import QuanChengSouSuoPinPaiTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoShangPin import QuanChengSouSuoShangPinTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeDengLu import WoDeDengLuTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeTuiChu import WoDeTuiChuTestCase

from utility.mailProcess import sendTestResultMail


if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    # root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    # reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/stability/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    suite.addTest(QuanChengSouSuoPinPaiTestCase("test_case"))
    suite.addTest(QuanChengSouSuoShangPinTestCase("test_case"))
    suite.addTest(QuanChengSouSuoMenDianTestCase("test_case"))
    suite.addTest(GouWuZhongXinTestCase("test_case"))
    suite.addTest(GuangChangSouSuoTestCase("test_case"))
    suite.addTest(GuangChangZhaoDianTestCase("test_case"))
    suite.addTest(PaiDuiQuHaoTestCase("test_case"))
    suite.addTest(GuangChangTingCheTestCase("test_case"))
    suite.addTest(GuangChangMaiDanTestCase("test_case"))
    suite.addTest(GuangChangMeiShiHuiTestCase("test_case"))
    suite.addTest(WoDeDengLuTestCase("test_case"))
    suite.addTest(WoDeTuiChuTestCase("test_case"))


    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'feifan_automation_test_report_ios.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)

    #if sentMail:
        #sendTestResultMail(reportpath, 'ios')
