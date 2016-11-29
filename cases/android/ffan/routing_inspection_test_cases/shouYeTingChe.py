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
# from pages.android.ffan.my_ffan_my_parking_payment_more_page import MyFfanMyParkingPaymentMorePage
# from pages.android.ffan.my_ffan_my_parking_payment_unbunding_page import MyFfanMyParkingPaymentUnbundingPage
# from pages.android.ffan.my_ffan_my_parking_payment_details_page import MyFfanMyParkingPaymentDetailsPage
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
    巡检 No.16
    用例名: 首页停车
    首页进入停车，查看停车交费，绑定车牌
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

    def testShouYeTingChe(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        parkingPage = ParkingCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingAddLicensePlatePage = ParkingAddLicensePlatePage(testcase = self,driver = self.driver,logger = self.logger)
#       parkingPaymentDetailsPage = MyFfanMyParkingPaymentDetailsPage(testcase = self,driver = self.driver,logger = self.logger)
#       parkingPaymentMorePage = MyFfanMyParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
#       parkingPaymentUnbundingPage = MyFfanMyParkingPaymentUnbundingPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnParkingCategory()
        parkingPage.validSelf()
        parkingPage.screenShot("tingChe")

        vehiclePlate = parkingPage.validVehiclePlateExist()
        if vehiclePlate:
            # Click "停车交费"， load parking payment.
            parkingPage.clickOnAddLicensePlate()
            parkingAddLicensePlatePage.validSelf()
            parkingAddLicensePlatePage.screenShot("tianJiaChePai")

            # Binding&Bunding VIN
            parkingAddLicensePlatePage.inputVIN()
            parkingAddLicensePlatePage.screenShot("tianJiaChePai")
            parkingAddLicensePlatePage.clickOnConfirmBtn()
            parkingAddLicensePlatePage.validManager()
            parkingAddLicensePlatePage.screenShot("cheLiangGuanLi")
            parkingAddLicensePlatePage.clickBackKey()
#         parkingPaymentDetailsPage.clickOnMore()
#         parkingPaymentMorePage.clickOnUnbundingBtn()
#         parkingPaymentUnbundingPage.clickOnUnbundingBtn()
#         parkingPaymentPage.validSelf()

        parkingAddLicensePlatePage.waitBySeconds(3)
        parkingPage.screenShot("tingChe")
        #检查入口项目
        itemList = (u"车牌管理", u"停车记录", u"停车券", u"帮助")
        titleList = (u"车牌管理", u"停车记录", u"停车优惠券", u"停车帮助")
        for i in range(len(titleList)):
            parkingAddLicensePlatePage.clickAndValidItems(itemList[i], titleList[i])

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