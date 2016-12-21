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
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_queue_page import SquareQueuePage
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
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.logger import logger


class GuangChangPaiDuiTestCase(TestCase):
    '''
    巡检 No.27
    用例名: 广场排队取号
    广场详情页点击排队取号进入排队取号页面，可以成功排队
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangpaidui/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangpaidui/screenshot/")
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

    def testGuangChangPaiDui(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        for i in range(INSIDELOOPNUM):
            logFile = "%sguangchangpaidui_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            # Load square page
            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "1")
            dashboardPage.clickOnSearchView()
            searchPage.validSelf()
            searchPage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "2")
            searchPage.inputText("北京通州万达广场")
            searchPage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "3")
            searchPage.clickOnSearch()
            searchPage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "4")
            searchPage.clickOnSearchResultFirstItem()
            squarePage.validSelf()
            squarePage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "5")
    
            # Click "排队取号"， load "排队取号" page.
            squarePage.clicOnQueue()
            queuePage.validSelf()
            queuePage.screenShotForStability("guangchangpaidui", self.loopNumer, str(i+1), "6")
    
            # Click "取号"
            if (queuePage.validGetQueue()):
                queuePage.clicOnQueueNumber()
                queuePage.waitBySeconds(2)
                queuePage.inputNumberOfMeals()
                queuePage.clicOnGetQueueNumber()
                queuePage.validQueueSuccess()

            queuePage.clickBackKey()
            squarePage.clickBackKey()
            searchPage.clickBackKey()

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangPaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
