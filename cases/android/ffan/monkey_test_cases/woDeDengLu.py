# -*- coding: utf-8 -*-

import os
import sys
import time
import glob
import shutil
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from tools.utility.constants import INSIDELOOPNUM
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
#from pages.android.ffan.login_verify_page import LoginVerifyPage
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.settings_page import SettingsPage
from cases.logger import logger


class WoDeDengLuTestCase(TestCase):
    '''
    巡检 No.49
    用例名 我的登录
    启动app，能够正常登陆
    '''
    def tearDown(self):
        if not os.path.exists(self.logcatFile):
            cmdLogcat = "adb logcat -d > %s" % (self.logcatFile)
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "wodedenglu/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "wodedenglu/screenshot/")
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

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testWoDeDengLu(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)

        for i in range(1):
            logFile = "%swodedenglu_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            dashboardPage.clickOnMy()
            myFfanPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "1")
            if myFfanPage.isLoginStatus():
                myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
                myFeiFanPage.clickOnSettings()

                settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
                dashboardPage.waitBySeconds()
                settingPage.validSelf()
                settingPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "2")
                settingPage.clickOnQuitAccountBtn()

                myFeiFanPage.waitBySeconds()
                myFeiFanPage.validLogoutStatusForStability()
                myFeiFanPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "3")
            myFfanPage.clickOnLogin()
            loginPage = LoginPage(self, self.driver, self.logger)
            loginPage.validSelf()
            loginPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "4")
            loginPage.switchToNormalLogin()
            loginPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "5")
            loginPage.inputUserName()
            loginPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "6")
            loginPage.inputPassWord()
            loginPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "7")
            loginPage.clickOnLoginBtn()
            myFfanPage.validSelf()
            myFfanPage.screenShotForStability("wodedenglu", self.loopNumer, str(i+1), "8")
            dashboardPage.waitBySeconds(seconds=2)

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeDengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)