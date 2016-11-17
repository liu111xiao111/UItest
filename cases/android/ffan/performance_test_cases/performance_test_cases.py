# -*- coding:utf-8 -*-

import sys,os

import time
import traceback
import threading

import HTMLTestRunner
from unittest.suite import TestSuite
from subprocess import Popen, PIPE
from utility.mailProcess import sendTestResultMail
from cases.android.ffan.common.performance import Performance
from cases.android.ffan.common.reportProcess import ReportHandle
from cases.android.ffan.common.performanceProcess import PerformanceHandle
from cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases


from cases.android.ffan.performance_test_cases.ffanDianYing import FFanDianYingTestCase
from cases.android.ffan.performance_test_cases.ffanMeiShiHui import FFanMeiShiHuiTestCase
from cases.android.ffan.performance_test_cases.ffanWoDeDengLu import FFanWoDeDengLuTestCase
from cases.android.ffan.performance_test_cases.ffanWoDeDingDan import FFanWoDeDingDanTestCase

def cmdPullFile(reportPath, caseName):
    cmdPullFile = "adb pull /sdcard/YCY/performance.xml %s" % reportPath
    Popen(cmdPullFile, shell=True, stdout=PIPE, stderr=PIPE)
    fileName = os.path.join(reportPath, 'performance.xml')
    fileNameNew = reportPath + "performance_" + caseName + ".xml"
    if (os.path.exists(fileName)):
        cmdChangeName = "mv performance.xml %s %s" % (fileName, fileNameNew)
        Popen(cmdChangeName, shell=True, stdout=PIPE, stderr=PIPE)

if __name__ == "__main__":
    # 生成Report目录
    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]
    #reportpath = "%s/report/ffan/%s/%s/" % ("/Users/songbo/workspace/autotest", time.strftime("%Y%m%d"), build_num)
    reportpath = "%s/report/perf/%s/%s/" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    # 添加测试用例
    suite = TestSuite()

#     suite.addTest(FFanDianYingTestCase("testFFanDianYing")) # 电影 No.06
#     suite.addTest(FFanMeiShiHuiTestCase("testFFanMeiShiHui")) # 美食汇 NO.7
    suite.addTest(FFanWoDeDingDanTestCase("testFFanWoDeDingDan")) # 我的订单 No.52
    cmdPullFile(reportpath, "wodedingdan")
#     suite.addTest(FFanWoDeDengLuTestCase("testFFanWoDeDengLu")) # 我的登录 No.49

    # 巡检及性能用例执行
    now = time.strftime('%H_%M_%S')

    filename = os.path.join(reportpath, 'feifan_automation_test_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')

    try:
        perf = Performance(reportpath)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        runner.run(suite)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'Traffic_performance_testcase.txt')
#         FpsPerformanceTestCases().getFpsPerf(reportpath)
        perf = Performance(reportpath)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        ColdBootTimePerformanceTestCases().getColdBootTime(reportpath)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime),'Traffic_performance_coldboottime.txt')
        perf = Performance(reportpath)
        startTraffic, sTime = perf.getTraffic()
        startTime = time.strftime('%Y/%m/%d %H:%M:%S')
        WarmBootTimePerformanceTestCases().getWarmBootTime(reportpath)
        endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'Traffic_performance_warmboottime.txt')
    except:
        raise traceback.format_exc()
    finally:
        pass
