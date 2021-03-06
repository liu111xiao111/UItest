#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import unittest

from utility.stabilityMailProcess import sendTestResultMail
from cases.android.ffan.monkey_test_cases.quanChengSouSuo import QuanChengSouSuoTestCase
from cases.android.ffan.monkey_test_cases.gouWuZhongXin import GouWuZhongXinTestCase
from cases.android.ffan.monkey_test_cases.meiShiHui import MeiShiHuiTestCase
from cases.android.ffan.monkey_test_cases.guangChangSouSuo import GuangChangSouSuoTestCase
from cases.android.ffan.monkey_test_cases.guangChangZhaoDian import GuangChangZhaoDianTestCase
from cases.android.ffan.monkey_test_cases.guangChangPaiDui import GuangChangPaiDuiTestCase
from cases.android.ffan.monkey_test_cases.guangChangTingChe import GuangChangTingCheTestCase
from cases.android.ffan.monkey_test_cases.guangChangMaiDan import GuangChangMaiDanTestCase
from cases.android.ffan.monkey_test_cases.woDeDengLu import WoDeDengLuTestCase
from cases.android.ffan.monkey_test_cases.woDeTuiChu import WoDeTuiChuTestCase
from tools.stabilityHandler import Handler
from tools.utility.constants import OUTLOOPNUM


class CrashError(Exception):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]

    # 飞凡数据存放路径
    reportPath = "%s/report/stability/%s/%s" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportPath):
        os.makedirs(reportPath)

    startTime = time.strftime('%Y/%m/%d %H:%M:%S')

    try:
        executeTimes = reportPath + "/executeTimes.txt"
        for i in range(OUTLOOPNUM):
            f = open(executeTimes, "w")
            f.write(str(i+1))
            f.close()
            # 添加测试用例
            suite = unittest.TestSuite()
            suite.addTest(QuanChengSouSuoTestCase("testQuanChengSouSuo")) # 全城搜索 No.03 123
            suite.addTest(GouWuZhongXinTestCase("testGouWuZhongXin")) # 购物中心 No.05 456
            suite.addTest(MeiShiHuiTestCase("testMeiShiHui")) # 美食汇 No.07
            suite.addTest(GuangChangSouSuoTestCase("testGuangChangSouSuo")) # 广场搜索 No.22
            suite.addTest(GuangChangZhaoDianTestCase("testGuangChangZhaoDian")) # 广场找店 No.24
            suite.addTest(GuangChangPaiDuiTestCase("testGuangChangPaiDui")) # 广场排队取号 No.27
            suite.addTest(GuangChangTingCheTestCase("testGuangChangTingChe")) # 广场停车 No.29
            suite.addTest(GuangChangMaiDanTestCase("testGuangChangMaiDan")) # 广场买单 No.30
            suite.addTest(WoDeTuiChuTestCase("testWoDeTuiChu")) # 我的退出 No.62
            suite.addTest(WoDeDengLuTestCase("testWoDeDengLu")) # 我的登录 No.49

            runner = unittest.TextTestRunner()
            runner.run(suite)

        handler = Handler('Android')
        resultsPath = "%s/report/stability/%s/%s" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if os.path.exists(resultsPath):
            handler.handle(resultsPath)

        if os.path.exists(executeTimes):
            os.remove(executeTimes)

    except CrashError as e:
        raise CrashError(e)
    finally:
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
#         startTime = '2016/12/29 16:54:36'
#         endTime = '2016/12/29 18:13:08'
        if sentMail:
            sendTestResultMail(startTime, endTime, reportPath, 'android')
