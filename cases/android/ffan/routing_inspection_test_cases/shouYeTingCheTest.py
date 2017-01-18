# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.parking_category_page import ParkingCategoryPage
from pages.android.ffan.parking_add_license_plate_page import ParkingAddLicensePlatePage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class ShouYeTingCheTestCase(TestCase):
    '''
    用例名: 首页停车
    首页进入停车，点击查看车牌管理，附近停车场，停车券，停车记录，帮助，绑定车牌（a:输入新车牌并绑定）
    '''

    def tearDown(self):
        logger.info("Driver quit")
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client initialize completed")

        TestPrepare(self, self.driver, self.logger).prepare()

    def testShouYeTingChe(self):
        # 爱逛街首页点击停车，进入停车页面，查看页面展示
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnParkingCategory()
        parkingPage = ParkingCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPage.validSelf()
        parkingPage.screenShot("tingChe")

        # 在停车页面点击查看车牌管理，停车记录，停车券，帮助查看跳转页面
        parkingAddLicensePlatePage = ParkingAddLicensePlatePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPage.screenShot("tingChe")
        #检查入口项目
        itemList = (u"车牌管理", u"停车记录", u"停车券", u"帮助")
        titleList = (u"车牌管理", u"停车记录", u"停车优惠券", u"停车帮助")
        for i in range(len(titleList)):
            parkingAddLicensePlatePage.clickAndValidItems(itemList[i], titleList[i])

        # 在停车页面点击添加车牌-输入车牌号-点击确定
        vehiclePlate = parkingPage.validVehiclePlateExist()
        if vehiclePlate:
            # 点击 "添加车牌"
            parkingPage.clickOnAddLicensePlate()
            parkingAddLicensePlatePage.validSelf()
            parkingAddLicensePlatePage.screenShot("tianJiaChePai")

            # 输入车牌号
            parkingAddLicensePlatePage.inputVIN()
            parkingAddLicensePlatePage.screenShot("tianJiaChePai")
            parkingAddLicensePlatePage.clickOnConfirmBtn()
            parkingAddLicensePlatePage.validManager()
            parkingAddLicensePlatePage.screenShot("cheLiangGuanLi")

        # 解绑车牌
        parkingAddLicensePlatePage.clickOnVehicleManager()
        parkingAddLicensePlatePage.validManager()
        parkingAddLicensePlatePage.screenShot("cheLiangGuanLi")
        parkingAddLicensePlatePage.clickOnVehiclePlate()
        parkingAddLicensePlatePage.screenShot("shanChuChePai")
        parkingAddLicensePlatePage.clickOnDeleteVehiclePlate()
        parkingAddLicensePlatePage.validManager()
        parkingAddLicensePlatePage.screenShot("tianJiaChePai")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShouYeTingCheTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)