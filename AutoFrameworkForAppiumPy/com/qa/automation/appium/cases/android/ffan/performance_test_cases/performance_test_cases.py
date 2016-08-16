# -*- coding: utf-8 -*-
from unittest import TestCase
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cpu_performance_test_cases import CpuPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.memory_performance_test_cases import MemoryPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases


class PerformanceTestCases(TestCase):
    '''
    作者 刘涛
    性能测试入口
    '''

    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_case(self):
        print("********** 性能测试：**********")
        print("CPU使用情况:             1")
        print("Memory使用情况:          2")
        print("App热启动时间：           3")
        print("App冷启动时间：           4")
        print("流畅度情况：              5")
        performanceTestNo = input(u"\n请输入性能测试序号： ")
        print("*****************************\n")
        cpuStatus = CpuPerformanceTestCases()
        memoryStatus = MemoryPerformanceTestCases()
        warmBootTime = WarmBootTimePerformanceTestCases()
        coldBootTime = ColdBootTimePerformanceTestCases()
        fpsStatus = FpsPerformanceTestCases()
        dicts = {1: cpuStatus.getCPU,
                 2: memoryStatus.getMemory,
                 3: warmBootTime.getWarmBootTime,
                 4: coldBootTime.getColdBootTime,
                 5: fpsStatus.getFps}
        if int(performanceTestNo) in dicts.keys():
            performanceTest = dicts.get(int(performanceTestNo))
            performanceTest()
        else:
            print("选择不在性能测试范围内！")


