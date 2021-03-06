# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.store_image_text_details_page import StoreImageTextDetailsPage
from com.qa.automation.appium.pages.android.ffan.store_info_page import StoreInfoPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class SquareRecommendCases(TestCase):
    '''
    巡检checklist No.: 35
    自动化测试case No.: 35
    广场详情页点击达人推荐可以进入门店详情页
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

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        tempText = squareModulePage.clickOnStaffPicks()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.validSelf()
        storeInfoPage.clickOnStoreImageTextDetails()

        storeImageTextDetailsPage = StoreImageTextDetailsPage(self , self.driver , self.logger)
        storeImageTextDetailsPage.validSelf()
        storeImageTextDetailsPage.validKeywords(tempText)
        storeImageTextDetailsPage.clickBackKey()

        storeInfoPage.validSelf()
        storeInfoPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        dashboardPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareRecommendCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test', description='Result for test')
    runner.run(suite)
