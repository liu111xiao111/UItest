# -*- coding:utf-8 -*-

import sys,os

import time
import traceback
import threading

import HTMLTestRunner
from unittest.suite import TestSuite
from utility.mailProcess import sendTestResultMail
from cases.android.ffan.common.performance import Performance
from cases.android.ffan.common.reportProcess import ReportHandle
from cases.android.ffan.common.performanceProcess import PerformanceHandle
from cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases


from cases.android.ffan.routing_inspection_test_cases.shanPingShouYe import ShanPingShouYeTestCase
from cases.android.ffan.routing_inspection_test_cases.chengShiQieHuan import ChengShiQieHuanTestCase
from cases.android.ffan.routing_inspection_test_cases.reCiSouSuo import ReCiSouSuoTestCase
from cases.android.ffan.routing_inspection_test_cases.dianYing import DianYingTestCase
from cases.android.ffan.routing_inspection_test_cases.meiShiHui import MeiShiHuiTestCase
from cases.android.ffan.routing_inspection_test_cases.pinPaiJie import PinPaiJieTestCase
from cases.android.ffan.routing_inspection_test_cases.qinZi import QinZiTestCase
from cases.android.ffan.routing_inspection_test_cases.qianDao import QianDaoTestCase
from cases.android.ffan.routing_inspection_test_cases.shangChao import ShangChaoTestCase
from cases.android.ffan.routing_inspection_test_cases.mingDianYouPin import MingDianYouPinTestCase
from cases.android.ffan.routing_inspection_test_cases.shouYeTingChe import ShouYeTingCheTestCase
from cases.android.ffan.routing_inspection_test_cases.maiDan import MaiDanTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangXiangQing import GuangChangXiangQingTestCase

from cases.android.ffan.routing_inspection_test_cases.huiShengHuo import HuiShengHuoTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangDianYingGuang import GuangChangDianYingGuangTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangYouHuiQuan import GuangChangYouHuiQuanTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangMeiShiHui import GuangChangMeiShiHuiTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangPaiDui import GuangChangPaiDuiTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangShiNeiDiTu import GuangChangShiNeiDiTuTestCase
from cases.android.ffan.routing_inspection_test_cases.woDeTingCheJiaoFei import WoDeTingCheJiaoFeiTestCase
from cases.android.ffan.routing_inspection_test_cases.guangChangTingChe import GuangChangTingCheTestCase
from cases.android.ffan.routing_inspection_test_cases.woDeLingHuaQian import WoDeLingHuaQianFeiTestCase
from cases.android.ffan.routing_inspection_test_cases.feiFanTongFuKuan import FeiFanTongFuKuanTestCase
from cases.android.ffan.routing_inspection_test_cases.feiFanTongKaGuanJia import FeiFanTongKaGuanJiaTestCase
from cases.android.ffan.routing_inspection_test_cases.feiFanTongLingHuaQian import FeiFanTongLingHuaQianTestCase


def runPerformance(reportPath):
    perf = Performance(reportPath)
    while True:
        perf.getCpu()
        perf.getMemory()
        perf.getTx()
        perf.getRx()

if __name__ == "__main__":
    # 生成Report目录
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/songbo/workspace/autotest", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    # 添加测试用例
    suite = TestSuite()

    suite.addTest(ShanPingShouYeTestCase("testShanPingShouYe")) # 闪屏首页 No.1
    suite.addTest(ChengShiQieHuanTestCase("testChengShiQieHuan_2")) # 城市切换 No.2
    suite.addTest(ReCiSouSuoTestCase("testReCiSouSuo")) # 热词搜索 No.4
    suite.addTest(DianYingTestCase("testDianYing")) # 电影 No.06
    suite.addTest(MeiShiHuiTestCase("testMeiShiHui")) # 美食汇 NO.7
    suite.addTest(PinPaiJieTestCase("testPinPaiJie")) # 品牌街 No.8
    suite.addTest(QinZiTestCase("testQinZi")) # 亲子 No.9
    suite.addTest(QianDaoTestCase("testQiandao")) # 签到 No.10
    suite.addTest(ShangChaoTestCase("testShangChao")) # 商超 No.11
    suite.addTest(MingDianYouPinTestCase("testMingDianYouPin")) # 名店优品 No.14
    suite.addTest(ShouYeTingCheTestCase("testShouYeTingChe")) # 首页停车 No.16
    suite.addTest(MaiDanTestCase("testMaiDan")) # 买单 No.17
    suite.addTest(GuangChangXiangQingTestCase("testGuangChangXiangQing")) # 广场详情 No.21


    suite.addTest(WoDeLingHuaQianFeiTestCase("testWoDeLingHuaQian")) # 我的零花钱 No.55
    suite.addTest(FeiFanTongFuKuanTestCase("testFeiFanTongFuKuan")) # 飞凡通付款 No.42
    suite.addTest(FeiFanTongKaGuanJiaTestCase("testFeiFanTongKaGuanJia")) # 飞凡通卡管家 No.43
    suite.addTest(FeiFanTongLingHuaQianTestCase("testFeiFanTongLingHuaQian")) # 飞凡通零花钱 No.44
    suite.addTest(HuiShengHuoTestCase("testHuiShenghuo")) # 惠生活 No.38
    suite.addTest(GuangChangDianYingGuangTestCase("testDianYingGuang")) # 广场电影逛 No.31
    suite.addTest(GuangChangYouHuiQuanTestCase("testYouHuiQuan")) # 广场优惠券 No.37
    suite.addTest(GuangChangMeiShiHuiTestCase("testGuangChangMeiShiHui")) # 广场美食汇 No.32
    suite.addTest(GuangChangPaiDuiTestCase("testGuangChangPaiDui")) # 广场排队 No.26
    suite.addTest(GuangChangShiNeiDiTuTestCase("testShiNeiDiTu")) # 广场室内地图 No.27
    suite.addTest(WoDeTingCheJiaoFeiTestCase("testWoDeTingCheJiaoFei")) # 我的停车缴费 No.57
    suite.addTest(GuangChangTingCheTestCase("testGuangChangTingChe")) # 广场停车 No.28




    # 巡检及性能用例执行
    now = time.strftime('%H_%M_%S')

    filename = os.path.join(reportpath, 'feifan_automation_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')

    perfThread = threading.Thread(target=runPerformance, args=(reportpath,))
    perfThread.setDaemon(True)
    perfThread.start()
    perf = Performance(reportpath)
    startTraffic, sTime = perf.getTraffic()
    startTime = time.strftime('%Y/%m/%d %H:%M:%S')
    runner.run(suite)

    try:
        FpsPerformanceTestCases().getFpsPerf(reportpath)
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath)
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath)
    except:
        raise traceback.format_exc()
    finally:
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTraffic(startTraffic, endTraffic, round(eTime-sTime))

        PerformanceHandle().Handle(startTime, endTime, reportpath)

        ReportHandle().handle(reportpath)

        if sentMail:
            sendTestResultMail(reportpath, 'android')
            from utility.performanceMailProcess import sendPerformanceMail
            sendPerformanceMail(startTime, endTime, reportpath, 'android')