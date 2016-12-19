# -*- coding:utf-8 -*-

import os
import sys
import time
import glob
import shutil
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from tools.utility.constants import INSIDELOOPNUM
from cases.android.ffan.common.monkey_process import MonkeyHandle
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.shopping_mall_page import ShoppingMallPage
from pages.android.ffan.dashboard_page import DashboardPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GouWuZhongXinTestCase(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 05
    自动化测试case No.: 05
    爱逛街进入购物中心确认广场距离排序顺序以及广场信息
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "gouwuzhongxin/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "gouwuzhongxin/screenshot/")
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

    def testGouWuZhongXin(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        shoppingMallPage = ShoppingMallPage(self, self.driver, self.logger)

        for i in range(INSIDELOOPNUM):
            logFile = "%sgouwuzhongxin_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            # Verify Home Page
            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("gouwuzhongxin", self.loopNumer, str(i+1), "1")

            # Enter Shopping Mall Page and Verify
            dashboardPage.clickOnShoppingMall()
            shoppingMallPage.validSelf()
            shoppingMallPage.screenShotForStability("gouwuzhongxin", self.loopNumer, str(i+1), "2")

            tabNumberList = (1,    # Total
                             2,    # Mall
                             3)    # Department
            for tabNumber in tabNumberList:
                shoppingMallPage.clickOnTab(tabNumber)
                shoppingMallPage.validListView()
                shoppingMallPage.validDistance()
                shoppingMallPage.screenShotForStability("gouwuzhongxin", self.loopNumer, str(i+1), str(tabNumber+2))
            shoppingMallPage.clickBackKey()

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GouWuZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
