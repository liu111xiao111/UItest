# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.parking_category_page import ParkingCategoryPage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_details_page import MyFfanMyParkingPaymentDetailsPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class ParkingBindingsCatergoryCases(TestCase):
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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        parkingPage = ParkingCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentPage = MyFfanMyParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentDetailsPage = MyFfanMyParkingPaymentDetailsPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboardPage.validSelf();
        dashboardPage.clickOnParkingCategory()
        parkingPage.validSelf();

        # Click "停车交费"， load parking payment.
        parkingPage.clickOnParkingPayment();
        parkingPaymentPage.validSelf();
        
        # Bunding VIN
        parkingPaymentPage.inputVIN();
        parkingPaymentPage.clickOnNextBtn();
        parkingPaymentDetailsPage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ParkingBindingsCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)