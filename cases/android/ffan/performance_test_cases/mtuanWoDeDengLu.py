# -*- coding: utf-8 -*-

import os
import sys
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from subprocess import Popen, PIPE
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_meituan
from configs.driver_configs import appPackage_meituan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from pages.android.meituan.dashboard_page import DashboardPage
from pages.android.meituan.login_page import LoginPage
from pages.android.meituan.my_meituan_page import MyMeituanPage
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.logger import logger


class MTuanWoDeDengLuTestCase(TestCase):
    '''
    巡检 No.1
    用例名 我的登录
    启动app，能够正常录
    '''
    def tearDown(self):
        if not os.path.exists(self.logcatFile):
            cmdLogcat = "adb logcat -d > %s" % (self.logcatFile)
            os.system(cmdLogcat)

        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logcatFile = "logcat.log"
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_meituan,
                                   appActivity_meituan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")

    def testMTuanWoDeDengLu(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/mtuan/wodedenglu" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)

        filename = "%s/logPortion.txt" % reportPath
        self.logcatFile = filename
        self.reset.clearLogcat()

        # 广播开始收集数据
        deviceID = DeviceInfoUtil().getDeviceID()
        cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.perfdaemon.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_meituan)
        Popen(cmdBroadcastStart, shell=True, stdout=PIPE, stderr=PIPE)

        # 用例执行
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("shouYe")
#         filename = "%s/logPortion.txt" % reportPath
#         #logcat_file = open(filename, 'w')
#         logcmd = "adb logcat -v time -s ActivityManager:I | grep [AppLaunch] > %s" % filename
#         #Poplog = Popen(logcmd,stdout=logcat_file,stderr=PIPE)
#         Popen(logcmd, shell=True, stdout=PIPE, stderr=PIPE)
        dashboardPage.clickOnMy()
        myMeituanPage = MyMeituanPage(self , self.driver , self.logger)
        myMeituanPage.validSelf()
        myMeituanPage.screenShot("woDe")
        loginStatus = myMeituanPage.validLoginStatus()
        if not loginStatus:
            myMeituanPage.clickOnSetting()
            myMeituanPage.screenShot("sheZhi")
            myMeituanPage.clickOnLogout()
            myMeituanPage.screenShot("woDe")

        myMeituanPage.clickOnLogin()
        loginPage = LoginPage(self , self.driver , self.logger)
        loginPage.screenShot("dengLu")
        loginPage.inputUserName()
        loginPage.screenShot("dengLu")
        loginPage.inputPassWord()
        loginPage.screenShot("dengLu")
        loginPage.clickOnLoginBtn()
        loginPage.screenShot("dengLu")

        # 取得logcat log
        cmdLogcat = "adb logcat -d > %s" % (filename)
        os.system(cmdLogcat)

        # 广播结束停止收集数据
        cmdBroadcastEnd = "adb shell am broadcast -a com.neusoft.perfdaemon.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_meituan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "adb pull /sdcard/Perf/perf.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MTuanWoDeDengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'MeiTuan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='MeiTuan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)