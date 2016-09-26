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
from com.qa.automation.appium.pages.ios.ffan.parking_payment_more_page import ParkingPaymentMorePage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_unbound_confirm_page import ParkingPaymentUnboundConfirmPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_page import ParkingPaymentPage
from com.qa.automation.appium.utility.logger import Logger


class ParkingPaymentBindingsCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #14
    自动化测试 #14-1
    首页进入停车，查看停车交费，绑定车牌
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
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentPage = ParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = ParkingPaymentMorePage(testcase=self, driver=self.driver, logger=self.logger)
        parkingPaymentUnboundConfirmPage = ParkingPaymentUnboundConfirmPage(testcase=self, driver=self.driver,
                                                                            logger=self.logger)

        # 首页点击停车
        dashboard.waitBySeconds(seconds=1)
        dashboard.validSelf()
        
        dashboard.clickOnParking()
        parkingPage.validSelf()
        
        parkingPage.clickOnZhaoche()
        parkingPage.validZhaoche()
        
        parkingPage.clickBackKey()
        
        parkingPage.clickOnFujintingche()
        parkingPage.validFujintingche()
        
        parkingPage.clickBackKey()
        
        parkingPage.clickOnTingchequan()
        parkingPage.validTingchequan()
        
        parkingPage.clickBackKey()
        
        parkingPage.clickOnHelp()
        parkingPage.validHelp()
        # 点击停车交费
        #parkingPage.clickOnParkingPayment()
        #parkingPaymentInputPlateNumberPage.validSelf()
        #parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)

        # 输入要绑定的车牌号
        #parkingPaymentInputPlateNumberPage.inputPlateNumber()
        #parkingPaymentInputPlateNumberPage.waitBySeconds(seconds=5)
        #parkingPaymentInputPlateNumberPage.clickOnNextStep()
        #parkingPaymentPage.validSelf()

        # 点击解除绑定
        #parkingPaymentPage.clickOnMore()
        #parkingPaymentMorePage.validSelf()
        #parkingPaymentMorePage.clickOnUnbundLicensePlate()
        #parkingPaymentUnboundConfirmPage.validSelf()
        #parkingPaymentUnboundConfirmPage.clickOnConfirm()
        #parkingPaymentInputPlateNumberPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ParkingPaymentBindingsCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
