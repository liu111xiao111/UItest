# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.parking_page import ParkingPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_input_plate_number_page import ParkingPaymentInputPlateNumberPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_page import ParkingPaymentPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_more_page import ParkingPaymentMorePage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_unbound_confirm_page import ParkingPaymentUnboundConfirmPage
from com.qa.automation.appium.utility.logger import Logger


class ParkingPaymentUnbindingCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #14
    自动化测试 #14-2
    首页进入停车，查看停车交费，解绑车牌
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage = ParkingPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentPage = ParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = ParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentUnboundConfirmPage = ParkingPaymentUnboundConfirmPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)

        # 首页点击停车
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnParking()
        parkingPage.validSelf()

        # 点击停车交费
        parkingPage.clickOnParkingPayment()
        parkingPaymentPage.validSelf()
        parkingPaymentPage.waitBySeconds(seconds=1)

        # 点击解除绑定
        parkingPaymentPage.clickOnMore()
        parkingPaymentMorePage.validSelf()
        parkingPaymentMorePage.clickOnUnbundLicensePlate()
        parkingPaymentUnboundConfirmPage.validSelf()
        parkingPaymentUnboundConfirmPage.clickOnConfirm()
        parkingPaymentInputPlateNumberPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ParkingPaymentUnbindingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)