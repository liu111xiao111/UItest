# -*- coding:utf-8 -*-

import os
import time
import logging
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.cinema_page import CinemaPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.popup_page import ClickActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.popup_page import PopupPage
from com.qa.automation.appium.pages.ios.ffan.popup_page import VerifyActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.seat_picking_page import SeatPickingPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.pages.ios.ffan.search_page import SearchPage


class SquareMovieCases(TestCase):
    '''
    作者 宋波
    巡检checklist #30
    自动化测试 #30
    广场详情页点击进入电影模块，检查数据正常并可以成功选座下单，取消订单
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        #dashboardPage.clickOnSquareModule()
        dashboardPage.clickOnSearchAll()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnMovie()

        cinemaPage = CinemaPage(self, self.driver, self.logger)
        cinemaPage.validSelf()
        tempText = cinemaPage.clickOnBuyTicket()

        popupPage = PopupPage(self , self.driver , self.logger)
        for tempTimes in range(3):
            self.logger.i("ATTEMPTS: %d" % (tempTimes + 1))
            if popupPage.validSelf(u"提示", VerifyActivityKeywordsType.NAME, False):
                popupPage.clickOnButton(u"是", ClickActivityKeywordsType.NAME)
                break
            popupPage.waitBySeconds()

        seatPickingPage = SeatPickingPage(self, self.driver, self.logger)
        seatPickingPage.validSelf()
        seatPickingPage.validKeywords(tempText)
        seatPickingPage.waitBySeconds(3)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareMovieCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
