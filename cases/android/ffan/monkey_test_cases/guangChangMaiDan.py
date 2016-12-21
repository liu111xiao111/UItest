# -*- coding: utf-8 -*-

import os
import sys
import time
import glob
import shutil
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

#from tools.utility.constants import INSIDELOOPNUM
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage;
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangMaiDanTestCase(TestCase):
    '''
    巡检checklist #27
    自动化测试 #27
    广场详情页点击进入乐付买单
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangmaidan/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangmaidan/screenshot/")
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

    def testGuangChangMaiDan(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        lefuPayPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)

        for i in range(1):
            logFile = "%sguangchangmaidan_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            # 绑定北京通州万达广场
            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "1")
            dashboardPage.clickOnSearchView()
            searchPage.validSelf()
            searchPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "2")
            searchPage.inputText("北京通州万达广场")
            searchPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "3")
            searchPage.clickOnSearch()
            searchPage.waitBySeconds(5)
            searchPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "4")
            searchPage.clickOnSearchResultFirstItem()
            squarePage.validSelf()
            squarePage.waitBySeconds(5)
            squarePage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "5")

            # Click "乐付买单"， load "乐付买单" page.
            squarePage.clicOnLefuPay()
            lefuPayPage.waitBySeconds(2)
            lefuPayPage.validSelf()
            lefuPayPage.waitBySeconds(2)
            lefuPayPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "6")
            # Click "乐付买单"， load detail pay page.
            lefuPayPage.clickOnLefuPay();
            lefuPayDetailPage.validSelf();
            lefuPayDetailPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "7")

            # Input money, click "确认买单".
            lefuPayDetailPage.inputMoney();
            lefuPayDetailPage.waitBySeconds(seconds=5)
            lefuPayDetailPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "8")
            lefuPayDetailPage.clickOnPay();
            lefuPayWayPage.validSelf();
            lefuPayWayPage.screenShotForStability("guangchangmaidan", self.loopNumer, str(i+1), "9")

#             lefuPayWayPage.waitBySeconds(10)
#             lefuPayWayPage.clickOnConfirm()
#             lefuPayWayPage.waitBySeconds(2)
#             lefuPayWayPage.clickBackKey()
#             lefuPayDetailPage.clickBackKey()
#             lefuPayDetailPage.waitBySeconds(2)
#             lefuPayPage.clickBackKey()
#             lefuPayPage.waitBySeconds(2)
#             squarePage.clickBackKey()
#             squarePage.waitBySeconds(2)
#             searchPage.clickBackKey()

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)