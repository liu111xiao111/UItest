# -*- coding: utf-8 -*-

import os
import sys
import time

import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from subprocess import Popen, PIPE
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.meituan.dashboard_page import DashboardPage
from pages.android.meituan.login_page import LoginPage
from pages.android.meituan.my_meituan_page import MyMeituanPage
from pages.android.meituan.my_meituan_my_order_page import MyMTuanMyOrderPage
from configs.driver_configs import appActivity_meituan
from configs.driver_configs import appPackage_meituan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class MTuanWoDeDingDanTestCase(TestCase):
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

    def testMTuanWoDeDingDan(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/mtuan/wodedingdan" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)
#         perf = Performance(reportPath)
#         startTraffic, sTime = perf.getTraffic()

        dashboardPage = DashboardPage(self , self.driver , self.logger)

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

        dashboardPage.clickOnMy()
        myMeituanPage = MyMeituanPage(self , self.driver , self.logger)
        myMeituanPage.validSelf()
        myMeituanPage.screenShot("woDe")
        loginStatus = myMeituanPage.validLoginStatus()
        if loginStatus:
            myMeituanPage.clickOnLogin()
            loginPage = LoginPage(self , self.driver , self.logger)
            loginPage.screenShot("dengLu")
            loginPage.inputUserName()
            loginPage.screenShot("dengLu")
            loginPage.inputPassWord()
            loginPage.screenShot("dengLu")
            loginPage.clickOnLoginBtn()
            loginPage.screenShot("dengLu")

        myMeituanPage.clickOnMyOrder()
        myOrderPage = MyMTuanMyOrderPage(self, self.driver, self.logger)
        myOrderPage.validSelf()
        myOrderPage.screenShot("woDeDingDan")
        myOrderPage.clickBackKey()
        myMeituanPage.validSelf()
        myMeituanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单待付款
        '''myMeituanPage.clickOnToBePaid()
        myMeituanPage.validSelfToBePaid()
        myMeituanPage.screenShot("woDeDaiFuKuan")
        myMeituanPage.clickBackKey()
        myMeituanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单可使用
        myMeituanPage.clickOnUse()
        myMeituanPage.validSelfUse()
        myMeituanPage.screenShot("woDeKeShiYong")
        myMeituanPage.clickBackKey()
        myMeituanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单我的点评
        myMeituanPage.clickOnComments()
        myMeituanPage.validSelfCommets()
        myMeituanPage.screenShot("woDeDianPing")
        myMeituanPage.clickBackKey()
        myMeituanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单退货退款
        myMeituanPage.clickOnReturnRefund()
        myMeituanPage.validSelfReturnRefund()
        myMeituanPage.screenShot("woDeTuiHuoTuiKuan")'''

        #cmdBroadcastEnd = "adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        cmdBroadcastEnd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_meituan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)

#         endTraffic, eTime = perf.getTraffic()
#         perf.parseTrafficData(startTraffic, endTraffic, round(eTime-sTime), 'traffic.txt')

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MTuanWoDeDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)