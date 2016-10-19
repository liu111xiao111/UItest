# -*- coding:utf-8 -*-

import os
import time
import logging
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.cinema_page import CinemaPage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.movie_details_page import MovieDetailsPage
from pages.android.ffan.movie_page import MoviePage
from pages.android.ffan.popup_page import ClickActivityKeywordsType
from pages.android.ffan.popup_page import PopupPage
from pages.android.ffan.popup_page import VerifyActivityKeywordsType
from pages.android.ffan.seat_picking_page import SeatPickingPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class DianYingTestCase(TestCase):
    '''
    巡检用例 No.06
    用例名: 电影
    首页进入电影模块，检查数据正常并可以进入选座页面
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

    def testDianYing(self):
        movieDetailsPage = MovieDetailsPage(self , self.driver , self.logger)
        seatPickingPage = SeatPickingPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        moviePage = MoviePage(self , self.driver , self.logger)
        cinemaPage = CinemaPage(self, self.driver, self.logger)
        popupPage = PopupPage(self , self.driver , self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnMovie()

        moviePage.validSelf()
        moviePage.clickOnSeatPickingAndBuyingTicket()

        movieDetailsPage.validSelf()
        movieDetailsPage.clickOnSubCinema()

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
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
