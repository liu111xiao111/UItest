# -*- coding: utf-8 -*-

import os
import sys
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from subprocess import Popen, PIPE
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from pages.android.ffan.login_page import LoginPage
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.settings_page import SettingsPage
from cases.logger import logger


class FFanWoDeDengLuTestCase(TestCase):
    '''
    巡检 No.49
    用例名 我的登录
    启动app，能够正常登陆
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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testFFanWoDeDengLu(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/ffan/wodedenglu" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)

        filename = "%s/logPortion.txt" % reportPath
        self.logcatFile = filename
        self.reset.clearLogcat()

        # 广播开始收集数据
        deviceID = DeviceInfoUtil().getDeviceID()
        cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        Popen(cmdBroadcastStart, shell=True, stdout=PIPE, stderr=PIPE)

        # 用例执行
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
#         filename = "%s/logPortion.txt" % reportPath
#         #logcat_file = open(filename, 'w')
#         logcmd = "adb logcat -v time -s ActivityManager:I | grep [AppLaunch] > %s" % filename
#         #Poplog = Popen(logcmd,stdout=logcat_file,stderr=PIPE)
#         Popen(logcmd, shell=True, stdout=PIPE, stderr=PIPE)
        dashboardPage.clickOnMy()
        myFfanPage.screenShot("woDe")
        if myFfanPage.isLoginStatus():
            myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
            myFeiFanPage.clickOnSettings()

            settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
            dashboardPage.waitBySeconds()
            settingPage.validSelf()
            settingPage.screenShot("sheZhi")
            settingPage.clickOnQuitAccountBtn()

            myFeiFanPage.waitBySeconds()
            myFeiFanPage.validLogoutStatus()
            myFeiFanPage.screenShot("woDe")
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(self, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.screenShot("dengLu")
        loginPage.switchToNormalLogin()
        loginPage.screenShot("puTongDengLu")
        loginPage.inputUserName()
        loginPage.screenShot("shuRuYongHuMing")
        loginPage.inputPassWord()
        loginPage.screenShot("shuRuMiMa")
        loginPage.clickOnLoginBtn()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")

        # 取得logcat log
        cmdLogcat = "adb logcat -d > %s" % (filename)
        os.system(cmdLogcat)

        # 广播结束停止收集数据
        cmdBroadcastEnd = "adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FFanWoDeDengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)