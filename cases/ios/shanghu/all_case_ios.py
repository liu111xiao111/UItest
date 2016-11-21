# -*- coding:utf-8 -*-

import sys, os
import time
from unittest import TestCase
from unittest import TestLoader
from unittest.suite import TestSuite

import HTMLTestRunner

from cases.ios.shanghu.common.reportProcess import ReportHandle

from cases.ios.shanghu.bianJiYuanGong import BianJiYuanGong
from cases.ios.shanghu.dengLu import DenggLuCase
from cases.ios.shanghu.dongJieYuanGong import DongJieYuanGong
from cases.ios.shanghu.jiaoYiGuanBiDingDan import JiaoYiGuanBiDingDan
from cases.ios.shanghu.jieDongYuanGong import JieDongYuanGong
from cases.ios.shanghu.jueSeLieBiao import JueSeLieBiao
from cases.ios.shanghu.quanBuDingDanZhuangTai import QuanBuDingDanZhuangTai
from cases.ios.shanghu.renYuanLiebiao import RenYuanLieBiao
from cases.ios.shanghu.shanchuYuanGong import ShanChuYuanGong
from cases.ios.shanghu.shangXueYuanRuKou import ShangXueYuanRuKou
from cases.ios.shanghu.tuiChuDengLu import TuiChuDengLuCase
from cases.ios.shanghu.xianShiQiangGouXiangXi import XianShiQiangGouXiangXi
from cases.ios.shanghu.xinZengJueSe import XinZengJueSe
from cases.ios.shanghu.xinZengYuanGong import XinZengYuanGongCase



from utility.mailProcess import sendTestResultMail



if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]


    # root_dir = os.path.dirname(
    #    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    # reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/report/shanghu/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()

    suite.addTest(BianJiYuanGong("test_case"))
    suite.addTest(DenggLuCase("test_case"))
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
