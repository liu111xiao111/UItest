# -*- coding: utf-8 -*-

import os
import sys
import time
#import datetime
from subprocess import Popen, PIPE
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.performance import Performance

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class FFanWoDeDingDanTestCase(TestCase):
    '''
    巡检 No.52
    用例名 我的订单
    查看我的订单信息及状态是否正确 
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def testFFanWoDeDingDan(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/ffan/wodedingdan" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)
        perf = Performance(reportPath)
        startTraffic, sTime = perf.getTraffic()
        #startTime = time.strftime('%Y/%m/%d %H:%M:%S')

        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)

        deviceID = DeviceInfoUtil().getDeviceID()
        #cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        cmdBroadcastStart = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        Popen(cmdBroadcastStart, shell=True, stdout=PIPE, stderr=PIPE)

        # 查看我的订单状态
#         timeList = []
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        myFfanPage.clickOnMyOrder()
        myOrderPage.validSelf()
        myOrderPage.screenShot("woDeDingDan")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        myOrderPage.clickBackKey()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))

        # 查看我的订单 -- 点击我的订单待付款
        myFfanPage.clickOnToBePaid()
        myFfanPage.validSelfToBePaid()
        myFfanPage.screenShot("woDeDaiFuKuan")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        myFfanPage.clickBackKey()
        myFfanPage.screenShot("woDe")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))

        # 查看我的订单 -- 点击我的订单可使用
        myFfanPage.clickOnUse()
        myFfanPage.validSelfUse()
        myFfanPage.screenShot("woDeKeShiYong")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        myFfanPage.clickBackKey()
        myFfanPage.screenShot("woDe")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))

        # 查看我的订单 -- 点击我的订单我的点评
        myFfanPage.clickOnComments()
        myFfanPage.validSelfCommets()
        myFfanPage.screenShot("woDeDianPing")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
        myFfanPage.clickBackKey()
        myFfanPage.screenShot("woDe")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))

        # 查看我的订单 -- 点击我的订单退货退款
        myFfanPage.clickOnReturnRefund()
        myFfanPage.validSelfReturnRefund()
        myFfanPage.screenShot("woDeTuiHuoTuiKuan")
#         timeList.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))

        #cmdBroadcastEnd = "adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        cmdBroadcastEnd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)

        #endTime = time.strftime('%Y/%m/%d %H:%M:%S')
        endTraffic, eTime = perf.getTraffic()
        perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'traffic.txt')
#         print(timeList)
#         print(len(timeList))
#         pageDisplayTime = []
#         for i in range(1, len(timeList)):
#             pageDisplayTime.append(float(timeList[i]) - float(timeList[i-1]))
#         print(pageDisplayTime)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FFanWoDeDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)