#!/usr/bin/env python
# coding:utf-8
import re
import os
import time
from subprocess import Popen, PIPE
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.utility.logger import Logger

class ParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FpsPerformanceTestCases():
    '''
    作者 宋波
    流畅度情况性能测试
    '''
    def getFpsPerf(self, reportPath):
        '''
        获取fps draw性能信息
        :param reportPath: 性能存储路径
        :return: 无
        '''
        try:
            self._setUp()
            dashboardPage = DashboardPage(self, self.driver, self.logger)
            tab_dict = {'我的'  : dashboardPage.clickOnMy,
                        '爱逛街': dashboardPage.clickLikeShopping,
                        '惠生活': dashboardPage.clickOnSmartLife,
                        '飞凡通': dashboardPage.clickOnFeiFanCard,
                        }
            for key, clickFunc in tab_dict.items():
                clickFunc()
                self._clearLog()
                time.sleep(30)
                self._getFps(key, reportPath)
        finally:
            self._tearDown()

    def _tearDown(self):
        '''
        释放appium client driver资源
        :return: 无
        '''
        self.driver.quit()

    def _setUp(self):
        '''
        初始化appium client driver, 跳出准备界面
        :return: 无
        '''
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(), deviceName_andr,
                                   driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def _clearLog(self):
        '''
        清理fps和draw信息
        :return: 无
        '''
        cmdFps = "adb shell dumpsys gfxinfo %s" % appPackage_ffan
        Popen(cmdFps, shell=True, stdout=PIPE, stderr=PIPE)

    def _getFps(self, tab, reportPath):
        '''
        获取获取fps和draw信息, 并保存生成日志文件
        :return: 无
        '''
        cmdFps = "adb shell dumpsys gfxinfo %s" % appPackage_ffan
        ret = Popen(cmdFps, shell=True, stdout=PIPE, stderr=PIPE)

        fpsInfo, err = ret.communicate()
        if err or not fpsInfo:
            return

        fpsInfo = fpsInfo.decode('utf-8')
        draw, fps = self._parseFps(fpsInfo)

        logName = "Fps_performance.txt"
        logPath = os.path.join(reportPath, logName)
        f = open(logPath, mode='a', encoding='utf-8')
        f.write("%s %s %s" % (tab, draw, fps) + "\n")
        f.close()

    def _parseFps(self, fpsInfo):
        '''
        解析Fps draw信息
        :param fpsInfo: 系统信息
        :return: draw and fps
        '''
        n = 0
        myFpss = []
        myDraws = []
        lines = fpsInfo.split('\n')
        for line in lines:
            try:
                if "View hierarchy:" in line:
                    break
                else:
                    draw, process, execute = re.findall(r'[0-9]+.[0-9]+', line)
                    draw = float(draw)
                    process = float(process)
                    execute = float(execute)
                    mydraw = round(draw, 2)
                    myfps = round(draw + process + execute, 2)
                    myFpss.append(myfps)
                    myDraws.append(mydraw)
            except Exception as e:
                pass
        if not len(myFpss) or not len(myDraws):
            raise ParseError('Parse app draw and fps failed.')
        AppDraw = round(sum(myDraws) / len(myDraws), 2)
        AppFps = round(sum(myFpss) / len(myFpss), 2)
        return AppDraw, AppFps
