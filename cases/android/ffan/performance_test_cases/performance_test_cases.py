# -*- coding:utf-8 -*-

import sys,os

import time
import traceback


import HTMLTestRunner
from unittest.suite import TestSuite
from cases.android.ffan.common.performance import Performance
from cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_meituan
from configs.driver_configs import appActivity_meituan
from cases.android.ffan.performance_test_cases.ffanDianYing import FFanDianYingTestCase
from cases.android.ffan.performance_test_cases.ffanMeiShiHui import FFanMeiShiHuiTestCase
from cases.android.ffan.performance_test_cases.ffanWoDeDengLu import FFanWoDeDengLuTestCase
from cases.android.ffan.performance_test_cases.ffanWoDeDingDan import FFanWoDeDingDanTestCase
from cases.android.ffan.performance_test_cases.mtuanWoDeDingDan import MTuanWoDeDingDanTestCase
from cases.android.ffan.performance_test_cases.mtuanWoDeDengLu import MTuanWoDeDengLuTestCase
from cases.android.ffan.performance_test_cases.mtuanMeiShi import MTuanMeiShiTestCase
from cases.android.ffan.performance_test_cases.mtuanDianYing import MTuanDianYingTestCase
from tools.performanceHandler import Handler


if __name__ == "__main__":

    # 通过参数却分每日多次执行版本
    build_num = sys.argv[1]

    # 飞凡数据存放路径
    reportpath_ffan = "%s/report/perf/%s/%s/ffan/" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_ffan):
        os.makedirs(reportpath_ffan)

    reportpath_ffan_coldboot = "%s/report/perf/%s/%s/ffan/coldboot" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_ffan_coldboot):
        os.makedirs(reportpath_ffan_coldboot)

    reportpath_ffan_warmboot = "%s/report/perf/%s/%s/ffan/warmboot" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_ffan_warmboot):
        os.makedirs(reportpath_ffan_warmboot)

    # 竞品数据存放路径
    reportpath_mtuan = "%s/report/perf/%s/%s/mtuan/" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_mtuan):
        os.makedirs(reportpath_mtuan)

    reportpath_mtuan_coldboot = "%s/report/perf/%s/%s/mtuan/coldboot" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_mtuan_coldboot):
        os.makedirs(reportpath_mtuan_coldboot)

    reportpath_mtuan_warmboot = "%s/report/perf/%s/%s/mtuan/warmboot" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath_mtuan_warmboot):
        os.makedirs(reportpath_mtuan_warmboot)

    # 添加测试用例
    suite = TestSuite()
    suite.addTest(FFanDianYingTestCase("testFFanDianYing")) # 电影 No.06
    suite.addTest(MTuanDianYingTestCase("testMTuanDianYing")) # 电影 No.06
    suite.addTest(FFanMeiShiHuiTestCase("testFFanMeiShiHui")) # 美食汇 NO.7
    suite.addTest(MTuanMeiShiTestCase("testMTuanMeiShi")) # 美食汇 NO.7
    suite.addTest(FFanWoDeDingDanTestCase("testFFanWoDeDingDan")) # 我的订单 No.52
    suite.addTest(MTuanWoDeDingDanTestCase("testMTuanWoDeDingDan")) # 我的订单 No.52
    suite.addTest(FFanWoDeDengLuTestCase("testFFanWoDeDengLu")) # 我的登录 No.49
    suite.addTest(MTuanWoDeDengLuTestCase("testMTuanWoDeDengLu")) # 我的登录 No.49

    # 用例执行
    now = time.strftime('%H_%M_%S')
    filename = os.path.join(reportpath_ffan, 'feifan_automation_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')

    try:
        # 巡检用例执行
        runner.run(suite)
 
        # 流畅度用例执行
        FpsPerformanceTestCases().getFpsPerf()
        FpsPerformanceTestCases().getFpsPerfJingpin()
  
        # 飞凡APP冷启动用例及流量统计执行
        perf = Performance(reportpath_ffan_coldboot)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath_ffan_coldboot, appPackage_ffan, appActivity_ffan)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime),'traffic.txt')
   
        # 飞凡APP热启动用例及流量统计执行
        perf = Performance(reportpath_ffan_warmboot)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath_ffan_warmboot, appPackage_ffan, appActivity_ffan)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'traffic.txt')
   
        # 美团APP冷启动用例及流量统计执行
        perf = Performance(reportpath_mtuan_coldboot)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath_mtuan_coldboot, appPackage_meituan, appActivity_meituan)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime),'traffic.txt')
   
        # 美团APP热启动用例及流量统计执行
        perf = Performance(reportpath_mtuan_warmboot)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath_mtuan_warmboot, appPackage_meituan, appActivity_meituan)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'traffic.txt')

        if os.path.exists(filename):
            os.remove(filename)

        handler = Handler()
        resultsPath = "%s/report/perf/%s/%s" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if os.path.exists(resultsPath):
            handler.handle(resultsPath)

    except:
        raise traceback.format_exc()
    finally:
        pass
