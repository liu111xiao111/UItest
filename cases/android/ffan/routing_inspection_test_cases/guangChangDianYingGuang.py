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
from pages.android.ffan.popup_page import ClickActivityKeywordsType
from pages.android.ffan.popup_page import PopupPage
from pages.android.ffan.popup_page import VerifyActivityKeywordsType
from pages.android.ffan.seat_picking_page import SeatPickingPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil

class GuangChangDianYingGuangTestCase(TestCase):
    '''
    巡检 No.32
    用例名: 广场电影逛
    广场详情页点击进入电影模块，检查数据正常并可以成功进入选座页面
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

    def testGuangChangDianYingGuang(self):
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        seatPickingPage = SeatPickingPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        popupPage = PopupPage(self , self.driver , self.logger)
        cinemaPage = CinemaPage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.validSelf()

        squareModulePage.clickOnMovie()
        cinemaPage.validSelf()

        # 判断影片是否未上映
        rtn = cinemaPage.validFilmRun()
        if not rtn:
            tempText = cinemaPage.clickOnBuyTicket()

            for tempTimes in range(3):
                logging.info("ATTEMPTS: %d" % (tempTimes + 1))
                if popupPage.validSelf("android:id/alertTitle", VerifyActivityKeywordsType.RESOURCE_ID, False):
                    popupPage.clickOnButton("android:id/button1", ClickActivityKeywordsType.RESOURCE_ID)
                    break
                popupPage.waitBySeconds()

            seatPickingPage.validSelf()
            seatPickingPage.validKeywords(tempText)
            seatPickingPage.waitBySeconds(seconds=2)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangDianYingGuangTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
