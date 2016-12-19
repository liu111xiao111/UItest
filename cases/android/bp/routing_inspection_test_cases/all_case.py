# -*- coding:utf-8 -*-

import sys, os
import time

from unittest.suite import TestSuite

import HTMLTestRunner

from cases.android.bp.common.reportProcess import ReportHandle
from cases.android.bp.routing_inspection_test_cases.dengLu import DengLuTestCase
from cases.android.bp.routing_inspection_test_cases.tuiChuDengLu import TuiChuDengLuTestCase
from cases.android.bp.routing_inspection_test_cases.renYuanLieBiao import RenYuanLieBiaoTestCase
from cases.android.bp.routing_inspection_test_cases.xinZengYuanGong import XinZengYuanGongTestCase
from cases.android.bp.routing_inspection_test_cases.bianJiYuanGong import BianJiYuanGongTestCase
from cases.android.bp.routing_inspection_test_cases.dongJieYuanGong import DongJieYuanGongTestCase
from cases.android.bp.routing_inspection_test_cases.jieDongYuanGong import JieDongYuanGongTestCase
from cases.android.bp.routing_inspection_test_cases.shanChuYuanGong import ShanChuYuanGongTestCase
from cases.android.bp.routing_inspection_test_cases.jueSeLieBiao import JueSeLieBiaoTestCase
from cases.android.bp.routing_inspection_test_cases.xinZengJueSe import XinZengJueSeTestCase
from cases.android.bp.routing_inspection_test_cases.leFuZhangDan import LeFuZhangDanTestCase
from cases.android.bp.routing_inspection_test_cases.shangXueYuan import ShangXueYuanTestCase


from utility.mailProcess import sendTestResultMail
from utility.messageProcess import sendTestResultMessage


if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]

    reportpath = "%s/report/shanghu/%s/%s/" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = TestSuite()
    #商户APP用例
    suite.addTest(RenYuanLieBiaoTestCase("testRenYuanLieBiao")) # 人员列表 No.3
    suite.addTest(XinZengYuanGongTestCase("testXinZengYuanGong")) # 新增员工 No.4
    suite.addTest(BianJiYuanGongTestCase("testBianJiYuanGong")) # 编辑员工 No.5
    suite.addTest(DongJieYuanGongTestCase("testDongJieYuanGong")) # 冻结员工 No.6
    suite.addTest(JieDongYuanGongTestCase("testJieDongYuanGong")) # 解冻员工 No.7
    suite.addTest(ShanChuYuanGongTestCase("testShanChuYuanGong")) # 删除员工 No.8
    suite.addTest(JueSeLieBiaoTestCase("testJueSeLieBiao")) # 角色列表 No.9
    suite.addTest(XinZengJueSeTestCase("testXinZengJueSe")) # 新增角色 No.10
    suite.addTest(LeFuZhangDanTestCase("testLeFuZhangDan")) # 乐付账单 No.13
    suite.addTest(ShangXueYuanTestCase("testShangXueYuan")) # 商学院 No.19
    suite.addTest(DengLuTestCase("testDengLu")) # 登录 No.1
    suite.addTest(TuiChuDengLuTestCase("testTuiChuDengLu")) # 退出登录 No.2
    now = time.strftime('%H_%M_%S')

    filename = reportpath + 'shanghu_automation_test_report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)

    ReportHandle().handle(reportpath)

    if sentMail:
        sendTestResultMail(reportpath, 'android')
        sendTestResultMessage('Android', 'shanghu')

