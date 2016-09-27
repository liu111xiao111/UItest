# -*- coding:utf-8 -*-

import sys,os

import time
import traceback
import threading

import HTMLTestRunner
from unittest.suite import TestSuite
from cases.android.ffan.common.performance import Performance
from cases.android.ffan.common.performanceProcess import PerformanceHandle
from cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases

from cases.android.ffan.routing_inspection_test_cases.huiShengHuo import HuiShengHuoTestCase
from cases.android.ffan.routing_inspection_test_cases.dianYingPiao import DianYingPiaoTestCase


def runPerformance(reportPath):
    perf = Performance(reportPath)
    while True:
        perf.getCpu()
        perf.getMemory()
        perf.getTx()
        perf.getRx()

if __name__ == "__main__":
    # 生成Report目录
    build_num = sys.argv[1]
    reportpath = "%s/report/ffan/%s/%s/" % ("/Users/ds/jenkins/workspace/android_allcaseauto/autotest/AutoFrameworkForAppiumPy", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    # 添加测试用例
    suite = TestSuite()

    suite.addTest(HuiShengHuoTestCase("testHuiShenghuo")) # 惠生活
    suite.addTest(DianYingPiaoTestCase("testDianYingPiao")) # 电影票



    # 巡检及性能用例执行
    now = time.strftime('%H_%M_%S')
    filename = os.path.join(reportpath, 'feifan_automation_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')

    perfThread = threading.Thread(target=runPerformance, args=(reportpath,))
    perfThread.setDaemon(True)
    perfThread.start()
    startTime = time.strftime('%Y/%m/%d %H:%M:%S')
    runner.run(suite)

    try:
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath)
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath)
        FpsPerformanceTestCases().getFpsPerf(reportpath)
    except:
        raise traceback.format_exc()
    finally:
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        PerformanceHandle().Handle(startTime, endTime, reportpath)
