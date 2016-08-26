# -*- coding:utf-8 -*-

import os
import time
import logging
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
from com.qa.automation.appium.pages.android.ffan.cinema_page import CinemaPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.popup_page import ClickActivityKeywordsType
from com.qa.automation.appium.pages.android.ffan.popup_page import PopupPage
from com.qa.automation.appium.pages.android.ffan.popup_page import VerifyActivityKeywordsType
from com.qa.automation.appium.pages.android.ffan.seat_picking_page import SeatPickingPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

class SquareMovieCases(TestCase):
    '''
    巡检checklist No.: 30
    自动化测试case No.: 30
    广场详情页点击进入电影模块，检查数据正常并可以成功选座下单，取消订单
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
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        seatPickingPage = SeatPickingPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        popupPage = PopupPage(self , self.driver , self.logger)
        cinemaPage = CinemaPage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage.validSelf()
        squareModulePage.waitBySeconds(5)
        squareModulePage.clickOnMovie()

        cinemaPage.validSelf()
        tempText = cinemaPage.clickOnBuyTicket()

        for tempTimes in range(3):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if popupPage.validSelf("android:id/alertTitle", VerifyActivityKeywordsType.RESOURCE_ID, False):
                popupPage.clickOnButton("android:id/button1", ClickActivityKeywordsType.RESOURCE_ID)
                break
            popupPage.waitBySeconds()

        seatPickingPage.validSelf()
        seatPickingPage.validKeywords(tempText)
        seatPickingPage.waitBySeconds(seconds=3)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareMovieCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath + 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
