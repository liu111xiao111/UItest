# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.parking_category_page import ParkingCategoryPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_details_page import MyFfanMyParkingPaymentDetailsPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_more_page import MyFfanMyParkingPaymentMorePage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_unbunding_page import MyFfanMyParkingPaymentUnbundingPage
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class ParkingBundingCatergoryCases(TestCase):
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
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        parkingPage = ParkingCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        parkingPaymentPage = MyFfanMyParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentDetailsPage = MyFfanMyParkingPaymentDetailsPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = MyFfanMyParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentUnbundingPage = MyFfanMyParkingPaymentUnbundingPage(testcase = self,driver = self.driver,logger = self.logger)

        # Load parking page
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(5)
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.validSelf()
        squareModulePage.waitBySeconds(5)
        squareModulePage.clickOnParking()
        parkingPage.validSelf()

        # Binding&Bunding VIN
        parkingPaymentPage.inputVIN()
        parkingPaymentPage.clickOnNextBtn()
        parkingPaymentDetailsPage.validSelf()
        parkingPaymentDetailsPage.clickOnMore()
        parkingPaymentMorePage.clickOnUnbundingBtn()
        parkingPaymentUnbundingPage.clickOnUnbundingBtn()
        parkingPaymentPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ParkingBundingCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath + 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)