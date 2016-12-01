# -*- coding:utf-8 -*-

import os
import sys
import time
import glob
import shutil
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from pages.android.ffan.settings_page import SettingsPage
from pages.android.ffan.login_page import LoginPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeTuiChuTestCase(TestCase):
    '''
    巡检 No.62
    用例名 我的退出
    退出登录，正常退出APP
    '''

    def tearDown(self):
        if not os.path.exists(self.logcatFile):
            cmdLogcat = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb logcat -d > %s" % (self.logcatFile)
            os.system(cmdLogcat)

        files = glob.glob('*.png')
        if files:
            for file in files:
                shutil.move(file, self.picturePath)
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/stability/%s/%s" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        self.reportpath = reportPath
        executeTimes = reportPath + "/executeTimes.txt"
        if os.path.exists(executeTimes):
            f = open(executeTimes, "r")
            loopNum = f.readline()
            f.close()
            print(loopNum)
            self.loopNumer = loopNum
        else:
            self.loopNumer = "100"
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "wodetuichu/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "wodetuichu/screenshot/")
        os.makedirs(self.picturePath)
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDeTuiChu(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)

        for i in range(2):
            logFile = "%swodetuichu_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            dashboardPage.waitBySeconds()
            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "1")
            dashboardPage.clickOnMy()

            myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
            myFeiFanPage.waitBySeconds()
            myFeiFanPage.validSelf()
            myFeiFanPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "2")
            if not myFeiFanPage.validLoginStatusForStability():
                myFfanPage.clickOnLogin()
                loginPage = LoginPage(self, self.driver, self.logger)
                loginPage.validSelf()
                loginPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "3")
                loginPage.switchToNormalLogin()
                loginPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "4")
                loginPage.inputUserName()
                loginPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "5")
                loginPage.inputPassWord()
                loginPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "6")
                loginPage.clickOnLoginBtn()
                myFfanPage.validSelf()
                myFfanPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "7")

            myFeiFanPage.clickOnSettings()

            settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
            dashboardPage.waitBySeconds()
            settingPage.validSelf()
            settingPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "8")
            settingPage.clickOnQuitAccountBtn()

            myFeiFanPage.waitBySeconds()
            myFeiFanPage.validLogoutStatus()
            myFeiFanPage.screenShotForStability("wodetuichu", self.loopNumer, str(i+1), "9")
            myFeiFanPage.clickOnDashboard()

            cmdLogcat = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTuiChuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
