# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from com.qa.automation.appium.pages.android.ffan.parking_category_page import ParkingCategoryPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class SquareParkingPaymentCases(TestCase):
    '''
        usage: No.26 广场详情页点击停车，正常进入停车模块
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
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.waitBySeconds(3)
        squareModulePage.validSelf()
        squareModulePage.clickOnParking()

        parkingPage = ParkingCategoryPage(self, self.driver, self.logger)
        parkingPaymentPage = MyFfanMyParkingPaymentPage(testcase=self, driver=self.driver, logger=self.logger)
        parkingPage.waitBySeconds(2)
        # 检查入口项目
        itemList = (u"附近停车场", u"停车券", u"停车记录", u"帮助")
        titleList = (u"停车场列表", u"停车优惠券", u"停车记录", u"停车帮助")
        for i in range(len(titleList)):
            parkingPaymentPage.clickAndValidItems(itemList[i], titleList[i])
            parkingPaymentPage.waitBySeconds(2)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareParkingPaymentCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
