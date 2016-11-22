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
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.meituan.dashboard_page import DashboardPage
from pages.android.meituan.movie_details_page import MovieDetailsPage
from pages.android.meituan.movie_page import MoviePage
from cases.logger import logger


class MTuanDianYingTestCase(TestCase):
    '''
    巡检用例 No.06
    用例名: 电影
    首页进入电影模块，检查数据正常并可以进入选座页面
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
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

    def testMTuanDianYing(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/mtuan/dianying" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)

        dashboardPage = DashboardPage(self, self.driver, self.logger)
        moviePage = MoviePage(self , self.driver , self.logger)
        movieDetailsPage = MovieDetailsPage(self , self.driver , self.logger)

        deviceID = DeviceInfoUtil().getDeviceID()
        #cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        cmdBroadcastStart = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_meituan)
        Popen(cmdBroadcastStart, shell=True, stdout=PIPE, stderr=PIPE)

        dashboardPage.validSelf()
        dashboardPage.screenShot("shouYe")

        filename = "%s/logPortion.txt" % reportPath
        #logcat_file = open(filename, 'w')
        logcmd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb logcat -v time -s ActivityManager:I | grep [AppLaunch] > %s" % filename
        #Poplog = Popen(logcmd,stdout=logcat_file,stderr=PIPE)
        Popen(logcmd, shell=True, stdout=PIPE, stderr=PIPE)

        dashboardPage.clickOnMovie()

        moviePage.validSelf()
        moviePage.screenShot("dianYing")
        moviePage.clickOnCheckAll()
        movieDetailsPage.validCheckall()
        movieDetailsPage.screenShot("dianYing")
        movieDetailsPage.clickOnBuyingTicket()

        movieDetailsPage.validSelf()
        movieDetailsPage.screenShot("dianYing")

        cmdBroadcastEnd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_meituan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)
 
        # 取得performance.xml文件
        cmdPull = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MTuanDianYingTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'MeiTuan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='MeiTuan_automation_test_report', description='Result for test')
    runner.run(suite)