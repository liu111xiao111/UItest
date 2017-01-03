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
from pages.android.ffan.food_category_page import FoodCategoryPage
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


class MeiShiHuiTestCase(TestCase):
    '''
    巡检 NO.7
    用例名: 美食汇
    首页进入美食正常进入找餐厅找优惠，数据显示正常可点击进入
    备注：由于版本变化，页面元素缺失，case无法通过
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
        self.logPath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "meishihui/log/")
        os.makedirs(self.logPath)
        self.picturePath = os.path.join(reportPath + "/" + self.loopNumer + "/" + "meishihui/screenshot/")
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

    def testMeiShiHui(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        foodPage = FoodCategoryPage(self, self.driver, self.logger)

        for i in range(INSIDELOOPNUM):
            logFile = "%smeishihui_%s_%s.log" % (self.logPath , self.loopNumer, str(i+1))
            self.logcatFile = logFile

            self.reset.clearLogcat()

            dashboardPage.validSelf()
            dashboardPage.screenShotForStability("meishihui", self.loopNumer, str(i+1), "1")

            dashboardPage.clickOnFood()
            foodPage.validFoodHomePage()
            foodPage.screenShotForStability("meishihui", self.loopNumer, str(i+1), "2")

            # 检查抢券入口
            foodPage.clickOnGrabCoupons()
            foodPage.validGrabCoupons()
            foodPage.screenShotForStability("meishihui", self.loopNumer, str(i+1), "3")
            foodPage.clickBackKey()

            # 检查美食分类及门店列表
            foodPage.validModulesForStability(self.loopNumer, str(i+1))
            foodPage.clickBackKey()

            cmdLogcat = "adb logcat -d > %s" % (logFile)
            os.system(cmdLogcat)

            files = glob.glob('*.png')
            if files:
                for file in files:
                    shutil.move(file, self.picturePath)

            # 生成HTML
            #MonkeyHandle().HandleForStability(logFile)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)