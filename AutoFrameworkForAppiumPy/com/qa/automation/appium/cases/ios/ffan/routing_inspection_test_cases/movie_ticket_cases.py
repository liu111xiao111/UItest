#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.cinema_page import CinemaPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.movie_details_page import MovieDetailsPage
from com.qa.automation.appium.pages.ios.ffan.movie_page import MoviePage
from com.qa.automation.appium.pages.ios.ffan.popup_page import ClickActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.popup_page import PopupPage
from com.qa.automation.appium.pages.ios.ffan.popup_page import VerifyActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.seat_picking_page import SeatPickingPage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(sys.path[0]))))))))))


class MovieTicketCases(TestCase):
    '''
    巡检checklist No.: 06
    自动化测试case No.: 06
    首页进入电影模块，检查数据正常并可以成功选座下单，支付并退票
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.valid_self()
        dashboardPage.clickOnMovie()

        moviePage = MoviePage(self , self.driver , self.logger)
        moviePage.validSelf()
        moviePage.clickOnSeatPickingAndBuyingTicket()

        movieDetailsPage = MovieDetailsPage(self , self.driver , self.logger)
        movieDetailsPage.validSelf()
        movieDetailsPage.clickOnSubCinema()

        cinemaPage = CinemaPage(self, self.driver, self.logger)
        cinemaPage.validSelf()
        tempText = cinemaPage.clickOnBuyTicket()

        popupPage = PopupPage(self , self.driver , self.logger)
        for tempTimes in range(3):
            print("ATTEMPTS: %d" % (tempTimes + 1))
            if popupPage.validSelf("android:id/alertTitle", VerifyActivityKeywordsType.RESOURCE_ID, False):
                popupPage.clickOnButton("android:id/button1", ClickActivityKeywordsType.RESOURCE_ID)
                break
            popupPage.waitBySeconds()

        seatPickingPage = SeatPickingPage(self, self.driver, self.logger)
        seatPickingPage.validSelf()
        seatPickingPage.validKeywords(tempText)
        seatPickingPage.clickBackKey()

        cinemaPage.waitBySeconds()
        cinemaPage.validSelf()
        cinemaPage.clickBackKey()

        movieDetailsPage.validSelf()
        movieDetailsPage.clickBackKey()

        moviePage.validSelf()
        moviePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MovieTicketCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
