# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.parking_page import ParkingPage
from pages.ios.ffan.parking_payment_input_plate_number_page import ParkingPaymentInputPlateNumberPage
from pages.ios.ffan.parking_payment_more_page import ParkingPaymentMorePage
from pages.ios.ffan.parking_payment_unbound_confirm_page import ParkingPaymentUnboundConfirmPage
from pages.ios.ffan.parking_payment_page import ParkingPaymentPage
from cases.logger import logger


class ShouYeTingCheTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #14
    自动化测试 #14-1
    首页进入停车，查看停车交费，绑定车牌
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage = ParkingPage(testcase = self, driver = self.driver, logger = self.logger)

        dashboard.waitBySeconds(seconds=1)
        dashboard.validSelf()

        # 首页点击停车
        dashboard.clickOnParking()
        parkingPage.validSelf()

        #点击车牌管理
        parkingPage.clickParkingManagement()
        parkingPage.validParkingManagement()

        #返回,验证
        parkingPage.clickBackKey()
        parkingPage.validSelf()

        parkingPage.clickOnTingchejilu()
        parkingPage.validTingchejilu()

        #返回,验证
        parkingPage.clickBackKey()
        parkingPage.validSelf()

        #点击停车券
        parkingPage.clickOnTingchequan()
        parkingPage.validTingchequan()

        # 返回,验证
        parkingPage.clickBackKey()
        parkingPage.validSelf()

        #点击附近停车场
        parkingPage.clickOnFujintingche()
        parkingPage.validFujintingche()

        # 返回,验证
        parkingPage.clickBackKey()
        parkingPage.validSelf()

        #点击帮助
        parkingPage.clickOnHelp()
        parkingPage.validHelp()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShouYeTingCheTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
