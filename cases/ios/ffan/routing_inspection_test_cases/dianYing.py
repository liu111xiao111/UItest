# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.cinema_page import CinemaPage
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.movie_details_page import MovieDetailsPage
from pages.ios.ffan.movie_page import MoviePage
from pages.ios.ffan.popup_page import ClickActivityKeywordsType
from pages.ios.ffan.popup_page import PopupPage
from pages.ios.ffan.popup_page import VerifyActivityKeywordsType
from pages.ios.ffan.seat_picking_page import SeatPickingPage
from utility.logger import Logger


class DianYingTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #6
    自动化测试 #6
    首页进入电影模块，检查数据正常并可以成功选座下单，支付并退票
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
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
            if popupPage.validSelf(u"提示", VerifyActivityKeywordsType.NAME, False):
                popupPage.clickOnButton(u"是", ClickActivityKeywordsType.NAME)
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
    suite = TestLoader().loadTestsFromTestCase(DianYingTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
