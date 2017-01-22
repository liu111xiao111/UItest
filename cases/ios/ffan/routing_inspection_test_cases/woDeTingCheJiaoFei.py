# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.parking_payment_input_plate_number_page import ParkingPaymentInputPlateNumberPage
from pages.ios.ffan.parking_payment_page import ParkingPaymentPage
from pages.ios.ffan.parking_payment_more_page import ParkingPaymentMorePage
from pages.ios.ffan.parking_payment_unbound_confirm_page import ParkingPaymentUnboundConfirmPage
from pages.ios.ffan.my_ffan_page import MyFfanPage
from cases.logger import logger


class WoDeTingCheJiaoFeiTestCase(TestCase):
    '''
    作者 刘涛
    我的停车缴费
    点击停车缴费，成功进入并显示正确数据
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
        parkingPaymentInputPlateNumberPage = ParkingPaymentInputPlateNumberPage(testcase = self,driver = self.driver,logger = self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)

        # 首页点击停车
        dashboard.waitBySeconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnMy()
        myFfanPage.validSelf()


        # 点击停车交费
        myFfanPage.clickOnParkingPayment()
        parkingPaymentInputPlateNumberPage.validSelf()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTingCheJiaoFeiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
