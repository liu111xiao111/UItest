# -*- coding: utf-8 -*-
from unittest import TestCase
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cpu_performance_test_cases import CpuPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.memory_performance_test_cases import MemoryPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.warm_boot_time_performance_test_cases import WarmBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.cold_boot_time_performance_test_cases import ColdBootTimePerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.fps_performance_test_cases import FpsPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.tx_performance_test_cases import TxPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.rx_performance_test_cases import RxPerformanceTestCases
from com.qa.automation.appium.cases.android.ffan.performance_test_cases.battery_temperature_performance_test_cases import BatteryTemperaturePerformanceTestCases


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
        print("APP热启动时间：           3")
        print("APP冷启动时间：           4")
        print("流畅度情况：              5")
        print("网络上行速率:             6")
        print("网络下行速率:             7")
        print("电池温度情况:             8")
        #print("电池电量情况:             9")
        performanceTestNo = input(u"\n请输入性能测试序号： ")
        print("*****************************\n")
        cpuStatus = CpuPerformanceTestCases()
        memoryStatus = MemoryPerformanceTestCases()
        warmBootTime = WarmBootTimePerformanceTestCases()
        coldBootTime = ColdBootTimePerformanceTestCases()
        fpsStatus = FpsPerformanceTestCases()
        Tx = TxPerformanceTestCases()
        Rx = RxPerformanceTestCases()
        batteryTemperature = BatteryTemperaturePerformanceTestCases()
        dicts = {1: cpuStatus.getCPU,
                 2: memoryStatus.getMemory,
                 3: warmBootTime.getWarmBootTime,
                 4: coldBootTime.getColdBootTime,
                 5: fpsStatus.getFps,
                 6: Tx.getTxBytes,
                 7: Rx.getRxBytes,
                 8: batteryTemperature.getBatteryTemperature}
        if int(performanceTestNo) in dicts.keys():
            performanceTest = dicts.get(int(performanceTestNo))
            performanceTest()
        else:
            print("选择不在性能测试范围内！")
