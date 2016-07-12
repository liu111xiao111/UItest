# -*- coding:utf-8 -*-

import os
import sys
import time

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.parking_page import ParkingPage;
from com.qa.automation.appium.pages.ios.ffan.parking_payment_input_plate_number_page import ParkingPaymentInputPlateNumberPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_page import ParkingPaymentPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_more_page import ParkingPaymentMorePage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_unbound_confirm_page import ParkingPaymentUnboundConfirmPage
from com.qa.automation.appium.utility.logger import Logger

import unittest
import HTMLTestRunner


class ParkingPaymentCases(unittest.TestCase):
    '''
        巡检checklist #14
        自动化测试 #14-1、#14-2、#56
        首页进入停车，查看停车交费，绑定/解绑车牌
        点击停车缴费，成功进入并显示正确数据
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

    def test_parking_bound_license_plate(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage = ParkingPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentPage = ParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboard.wait_by_seconds(seconds=1)
        dashboard.valid_self()
        dashboard.click_Parking()
        parkingPage.validSelf()

        # Load parking payment page
        parkingPage.clickOnParkingPayment()
        parkingPaymentInputPlateNumberPage.validSelf()
        parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)

        # Input license plate
        parkingPaymentInputPlateNumberPage.inputPlateNumber()
        parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)
        parkingPaymentInputPlateNumberPage.clickOnNextStep()
        parkingPaymentPage.validSelf()

    def test_parking_unbound_license_plate(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage = ParkingPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentPage = ParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = ParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentUnboundConfirmPage = ParkingPaymentUnboundConfirmPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboard.wait_by_seconds(seconds=1)
        dashboard.valid_self()
        dashboard.click_Parking()
        parkingPage.validSelf()

        # Load parking payment page
        parkingPage.clickOnParkingPayment()
        parkingPaymentPage.validSelf()
        parkingPaymentPage.waitBySeconds(seconds=1)

        # Unbound license plate
        parkingPaymentPage.clickOnMore()
        parkingPaymentMorePage.validSelf()
        parkingPaymentMorePage.clickOnUnbundLicensePlate()
        parkingPaymentUnboundConfirmPage.validSelf()
        parkingPaymentUnboundConfirmPage.clickOnConfirm()
        parkingPaymentInputPlateNumberPage.validSelf()

    def test_my_feifan_parking_payment(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage = ParkingPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentPage = ParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = ParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentUnboundConfirmPage = ParkingPaymentUnboundConfirmPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboard.wait_by_seconds(seconds=1)
        dashboard.valid_self()
        dashboard.click_Parking()
        parkingPage.validSelf()

        # Load parking payment page
        parkingPage.clickOnParkingPayment()
        parkingPaymentInputPlateNumberPage.validSelf()
        parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)

        # Input license plate
        parkingPaymentInputPlateNumberPage.inputPlateNumber()
        parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)
        parkingPaymentInputPlateNumberPage.clickOnNextStep()
        parkingPaymentPage.validSelf()

        # Unbound license plate
        parkingPaymentPage.clickOnMore()
        parkingPaymentMorePage.validSelf()
        parkingPaymentMorePage.clickOnUnbundLicensePlate()
        parkingPaymentUnboundConfirmPage.validSelf()
        parkingPaymentUnboundConfirmPage.clickOnConfirm()
        parkingPaymentInputPlateNumberPage.validSelf()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ParkingPaymentCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)