# -*- coding: utf-8 -*-

import os
import sys
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from subprocess import Popen, PIPE
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.food_category_page import FoodCategoryPage
#from pages.android.ffan.sales_promotion_page import SalesPromotionPage
#from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
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


class FFanMeiShiHuiTestCase(TestCase):
    '''
    巡检 NO.7
    用例名: 美食汇
    首页进入美食正常进入找餐厅找优惠，数据显示正常可点击进入
    备注：由于版本变化，页面元素缺失，case无法通过
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

    def testFFanMeiShiHui(self):
        build_num = sys.argv[1]
        reportPath = "%s/report/perf/%s/%s/ffan/meishihui" % ("/Users/uasd-qiaojx/Desktop", time.strftime("%Y%m%d"), build_num)
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)

        dashboardPage = DashboardPage(self, self.driver, self.logger)
        foodPage = FoodCategoryPage(self, self.driver, self.logger)
        #salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        #lefuPage = SquareLefuPayPage(self, self.driver, self.logger)

        deviceID = DeviceInfoUtil().getDeviceID()
        #cmdBroadcastStart = "adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        cmdBroadcastStart = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb -s %s shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle true" % (deviceID, appPackage_ffan)
        Popen(cmdBroadcastStart, shell=True, stdout=PIPE, stderr=PIPE)

        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        filename = "%s/logPortion.txt" % reportPath
        #logcat_file = open(filename, 'w')
        logcmd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb logcat -v time -s ActivityManager:I | grep [AppLaunch] > %s" % filename
        #Poplog = Popen(logcmd,stdout=logcat_file,stderr=PIPE)
        Popen(logcmd, shell=True, stdout=PIPE, stderr=PIPE)

        dashboardPage.clickOnFood()
        foodPage.validFoodHomePage()
        foodPage.screenShot("meiShiHui")

        # 检查所有子界面入口
#         foodPage.validModules()

        cmdBroadcastEnd = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb shell am broadcast -a com.neusoft.ycy.PERFORMANCE_TEST --es packageName %s --ez launchServiceToogle false" % appPackage_ffan
        Popen(cmdBroadcastEnd, shell=True, stdout=PIPE, stderr=PIPE)

        # 取得performance.xml文件
        cmdPull = "/Users/uasd-qiaojx/Desktop/tools/android-sdk/platform-tools/adb pull /sdcard/YCY/performance.xml %s" % reportPath
        Popen(cmdPull, shell=True, stdout=PIPE, stderr=PIPE)

        '''# 检查优惠打折
        foodPage.clickOnCoupon()
        salesPromotionPage.validSelf()
        salesPromotionPage.clickBackKey()

        # 检查抢券
        oodPage.clickOnGrabCoupons()
        salesPromotionPage.validSelfCoupon()
        salesPromotionPage.clickBackKey()

        # 检查乐付
        foodPage.clickOnLePay()
        lefuPage.validSelf()'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FFanMeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)