# -*- coding:utf-8 -*-

import sys, os
import time
from unittest import TestCase
from unittest import TestLoader
from unittest.suite import TestSuite

import HTMLTestRunner

from cases.ios.bp.common.reportProcess import ReportHandle

from cases.ios.bp.bianJiYuanGong import BianJiYuanGong
from cases.ios.bp.dengLu import DenggLu
from cases.ios.bp.dongJieYuanGong import DongJieYuanGong
from cases.ios.bp.jiaoYiGuanBiDingDan import JiaoYiGuanBiDingDan
from cases.ios.bp.jieDongYuanGong import JieDongYuanGong
from cases.ios.bp.jueSeLieBiao import JueSeLieBiao
from cases.ios.bp.quanBuDingDan import QuanBuDingDanZhuangTai
from cases.ios.bp.renYuanLieBiao import RenYuanLieBiao
from cases.ios.bp.shanchuYuanGong import ShanChuYuanGong
from cases.ios.bp.shangXueYuan import ShangXueYuanRuKou
from cases.ios.bp.tuiChuDengLu import TuiChuDengLuCase
from cases.ios.bp.xianShiQiangGou import XianShiQiangGouXiangXi
from cases.ios.bp.xinZengJueSe import XinZengJueSe
from cases.ios.bp.xinZengYuanGong import XinZengYuanGongCase
from utility.messageProcess import sendTestResultMessage



from utility.mailProcess import sendTestResultMail



if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    # root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    # reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/report/bp/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    suite.addTest(BianJiYuanGong("test_case"))
    suite.addTest(DenggLu("test_case"))
    suite.addTest(DongJieYuanGong("test_case"))
    suite.addTest(JiaoYiGuanBiDingDan("test_case"))
    suite.addTest(JieDongYuanGong("test_case"))
    suite.addTest(JueSeLieBiao("test_case"))
    suite.addTest(QuanBuDingDanZhuangTai("test_case"))
    suite.addTest(RenYuanLieBiao("test_case"))
    #suite.addTest(ShanChuYuanGong("test_case"))
    suite.addTest(TuiChuDengLuCase("test_case"))
    suite.addTest(XianShiQiangGouXiangXi("test_case"))
    suite.addTest(XinZengJueSe("test_case"))
    suite.addTest(XinZengYuanGongCase("test_case"))
    suite.addTest(ShangXueYuanRuKou("test_case"))



    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'shanghu_automation_test_report_ios.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report_ios',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)


    if sentMail:
        sendTestResultMail(reportpath, 'ios')
        # sendTestResultMessage('ios')
        sendTestResultMessage('IOS', 'bp')
