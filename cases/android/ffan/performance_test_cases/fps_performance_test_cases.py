#!/usr/bin/env python
# coding:utf-8
import re
import sys,os
import time
from unittest import TestCase
from subprocess import Popen, PIPE
from pages.android.ffan.dashboard_page import DashboardPage as FFANDP
from pages.android.meituan.dashboard_page import DashboardPage as MTUANDP
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import appPackage_meituan
from configs.driver_configs import appActivity_meituan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger

class ParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FpsPerformanceTestCases(TestCase):
    '''
    作者 宋波
    流畅度情况性能测试
    '''
    def getFpsPerf(self):
        '''
        获取fps draw性能信息
        :param reportPath: 性能存储路径
        :return: 无
        '''
        try:
            self._setUp()
            build_num = sys.argv[1]
            reportPath = "%s/report/perf/%s/%s/ffan/fps" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
            if not os.path.exists(reportPath):
                os.makedirs(reportPath)
            dashboardPage = FFANDP(self, self.driver, self.logger)
            tab_dict = {'Mine'  : dashboardPage.clickOnMy,
                        'Dashboard': dashboardPage.clickLikeShopping,
                        'BenefitsLife': dashboardPage.clickOnSmartLife,
                        'FfanWallet': dashboardPage.clickOnFeiFanCard,
                        }
            for key, clickFunc in tab_dict.items():
                clickFunc()
                self._clearLog()
                dashboardPage.scrollOnPage()
                self._getFps(key, reportPath, appPackage_ffan)
        finally:
            self._tearDown()

    def getFpsPerfJingpin(self):
        '''
        获取fps draw性能信息
        :param reportPath: 性能存储路径
        :return: 无
        '''
        try:
            self._setUpJingpin()
            build_num = sys.argv[1]
            reportPath = "%s/report/perf/%s/%s/mtuan/fps" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
            if not os.path.exists(reportPath):
                os.makedirs(reportPath)
            dashboardPage = MTUANDP(self, self.driver, self.logger)
            tab_dict = {'Mine'  : dashboardPage.clickOnMy,
                        'Dashboard': dashboardPage.clickOnDashboard,
                        }
            for key, clickFunc in tab_dict.items():
                clickFunc()
                self._clearLog()
                dashboardPage.scrollOnPage()
                self._getFps(key, reportPath, appPackage_meituan)
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
        self.version = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr,
                                   self.version, deviceName_andr,
                                   driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def _setUpJingpin(self):
        '''
        初始化appium client driver, 跳出准备界面
        :return: 无
        '''
        self.logger = Logger()
        self.version = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_meituan, appActivity_meituan, platformName_andr,
                                   self.version, deviceName_andr,
                                   driver_url).getDriver()

    def _clearLog(self):
        '''
        清理fps和draw信息
        :return: 无
        '''
        cmdFps = "adb shell dumpsys gfxinfo %s" % appPackage_ffan
        Popen(cmdFps, shell=True, stdout=PIPE, stderr=PIPE)

    def _getFps(self, tab, reportPath, pkName):
        '''
        获取获取fps和draw信息, 并保存生成日志文件
        :return: 无
        '''
        cmdFps = "adb shell dumpsys gfxinfo %s" % pkName
        ret = Popen(cmdFps, shell=True, stdout=PIPE, stderr=PIPE)

        fpsInfo, err = ret.communicate()
        if err or not fpsInfo:
            return

        fpsInfo = fpsInfo.decode('utf-8')
        draw, fps = self._parseFps(fpsInfo)

        logName = "fps.txt"
        logPath = os.path.join(reportPath, logName)
        f = open(logPath, mode='a', encoding='utf-8')
        f.write("%s %s %s" % (tab, draw, fps) + "\n")
        f.close()

    def _getFpsLogName(self, tab, reportPath, logName = "default"):
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

        logName = logName
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
                    if int(self.version.split(".")[0]) < 5:
                        draw, process, execute = re.findall(r'[0-9]+.[0-9]+', line)
                        draw = float(draw)
                        process = float(process)
                        execute = float(execute)
                        mydraw = round(draw, 2)
                        myfps = round(draw + process + execute, 2)
                    else:
                        draw, prepare, process, execute = re.findall(r'[0-9]+.[0-9]+', line)
                        draw = float(draw)
                        prepare = float(prepare)
                        process = float(process)
                        execute = float(execute)
                        mydraw = round(draw, 2)
                        myfps = round(draw + prepare + process + execute, 2)
                    myFpss.append(myfps)
                    myDraws.append(mydraw)
            except Exception as e:
                pass
        if not len(myFpss) or not len(myDraws):
            raise ParseError('Parse app draw and fps failed.')
        AppDraw = round(sum(myDraws) / len(myDraws), 2)
        AppFps = round(sum(myFpss) / len(myFpss), 2)
        return AppDraw, AppFps
