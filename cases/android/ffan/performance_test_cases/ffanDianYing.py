# -*- coding:utf-8 -*-

import os
import time
import sys
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from subprocess import Popen, PIPE
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.movie_details_page import MovieDetailsPage
from pages.android.ffan.movie_page import MoviePage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class FFanDianYingTestCase(TestCase):
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

    def testFFanDianYing(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/ffan/dianying" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)

        movieDetailsPage = MovieDetailsPage(self , self.driver , self.logger)
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        moviePage = MoviePage(self , self.driver , self.logger)

        deviceID = DeviceInfoUtil().getDeviceID()
        #cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        cmdBroadcastStart = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
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
        moviePage.clickOnSeatPickingAndBuyingTicket()

        movieDetailsPage.validSelf()
        movieDetailsPage.screenShot("dianYing")

        #Poplog.terminate()


        cmdBroadcastEnd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FFanDianYingTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
