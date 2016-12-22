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
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.search_result_store_page import SearchResultStorePage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangSouSuoTestCase(TestCase):
    '''
    巡检 No.22
    用例名 广场搜索
    首页进入广场详情页， 广场详情页点击搜索进入搜索，搜索服务和门店，有正常结果显示（广场维度）
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangsousuo/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "guangchangsousuo/screenshot/")
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

    def testGuangChangSouSuo(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        for i in range(INSIDELOOPNUM):
            logFile = "%sguangchangsousuo_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "1")
            dashboardPage.clickOnSearchView()
            searchPage.validSelf()
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "2")
            searchPage.inputText("北京通州万达广场")
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "3")
            searchPage.waitBySeconds(2)
            searchPage.clickOnSearch()
            searchPage.waitBySeconds(2)
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "4")
            searchPage.clickOnSearchResultFirstItem()
            squareModulePage.waitBySeconds(2)
            squareModulePage.validSelf()
            squareModulePage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "5")
            squareModulePage.clickOnSearch()

            searchPage.validSelf()
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "6")
            searchPage.inputGuangChangStoreName()
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "7")
            searchPage.clickOnSearch()
            searchPage.validSearchResult(u"帝娜朵拉", "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
            #tempText = searchPage.clickOnSearchResultFirstItem()
            searchPage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "8")
            searchPage.clickOnFindStoreFirstItem()

            searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
            #searchResultStorePage.validKeywords(tempText)
            searchResultStorePage.validSelf()
            searchResultStorePage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "9")
            searchResultStorePage.clickBackKey()
            searchResultStorePage.screenShotForStability("guangchangsousuo", self.loopNumer, str(i+1), "10")

            searchPage.clickBackKey()
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
    suite = TestLoader().loadTestsFromTestCase(GuangChangSouSuoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
