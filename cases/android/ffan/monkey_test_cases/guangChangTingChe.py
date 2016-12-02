# -*- coding: utf-8 -*-

import os
import sys
import time
import glob
import shutil
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.parking_category_page import ParkingCategoryPage
from pages.android.ffan.square_module_page import SquareModulePage
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangTingCheTestCase(TestCase):
    '''
    巡检 No.29
    用例名: 广场停车
    点击停车缴费，成功进入并显示正确数据
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangtingche/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangtingche/screenshot/")
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

    def testGuangChangTingChe(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)

        for i in range(1):
            logFile = "%sguangchangtingche_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "1")
            dashboardPage.clickOnSearchAll()

            searchPage = SearchPage(self, self.driver, self.logger)
            searchPage.validSelf()
            searchPage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "2")
            searchPage.inputKeywords(u"北京通州万达广场")
            searchPage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "3")
            searchPage.clickOnSearch()
            searchPage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "4")
            searchPage.clickOnSearchResultFirstItem()

            squareModulePage = SquareModulePage(self, self.driver, self.logger)
            squareModulePage.validSelf()
            squareModulePage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "5")
            squareModulePage.clickOnParking()

            parkingPage = ParkingCategoryPage(self, self.driver, self.logger)
            parkingPage.waitBySeconds(2)
            parkingPage.validSelf()
            parkingPage.screenShotForStability("guangchangtingche", self.loopNumer, str(i+1), "6")
            parkingPage.clickBackKey()
            squareModulePage.clickBackKey()
            searchPage.clickBackKey()

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangTingCheTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
