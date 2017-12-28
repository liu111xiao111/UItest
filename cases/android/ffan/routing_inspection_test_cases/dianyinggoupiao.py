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
from pages.android.ffan.movie_goupiao_page import Moviegoupiaopage
from pages.android.ffan.seat_picking_page import SeatPickingPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class DianYingGouPiaoTestCase(TestCase):
    '''
    巡检用例 No.06
    用例名: 电影
    首页进入电影模块，检查数据正常并可以进入选座页面
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        moviegoupiaopage = Moviegoupiaopage(self , self.driver , self.logger)
        i = 1
        while i < 8:
            city =  moviegoupiaopage.validcity()
            if city:
                return i == 10
            moviegoupiaopage.clickBackKey()
            time.sleep(3)
            i =  i+1
        moviegoupiaopage.clickchengshi()
        time.sleep(5)
        moviegoupiaopage.clickonbeijing()
        time.sleep(5)
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare()


    def testDianYinggoupiao(self):

        dashboardPage = DashboardPage(self , self.driver , self.logger)
        popupPage = PopupPage(self , self.driver , self.logger)
        moviegoupiaopage = Moviegoupiaopage(self , self.driver , self.logger)

        dashboardPage.validSelf()
        moviegoupiaopage.clickchengshi()
        time.sleep(5)
        moviegoupiaopage.clickanyang()
        time.sleep(5)
        dashboardPage.clickOnMovie()
        time.sleep(5)
        moviegoupiaopage.clickOnyingpian()
        time.sleep(5)
        moviegoupiaopage.clickonpingpai()
        time.sleep(5)
        moviegoupiaopage.clickhengdian()
        time.sleep(5)
        moviegoupiaopage.clickyingyuanxiangqing()
        time.sleep(5)
        moviegoupiaopage.clickOnbuy()
        time.sleep(5)
        moviegoupiaopage.clickxuanzuo()
        time.sleep(5)
        moviegoupiaopage.clickxuanhaole()
        time.sleep(5)
        moviegoupiaopage.clicktijaiodingdan()
        time.sleep(5)
        moviegoupiaopage.validSelf()
        time.sleep(5)
        moviegoupiaopage.clickfanhui()
        time.sleep(5)
        moviegoupiaopage.clickfanhui()
        time.sleep(5)
        moviegoupiaopage.clickfanhui()
        time.sleep(5)
        moviegoupiaopage.clickfanhui()
        time.sleep(5)
        moviegoupiaopage.clickfanhui()
        time.sleep(5)
        moviegoupiaopage.clickchengshi()
        time.sleep(5)
        moviegoupiaopage.clickonbeijing()
        time.sleep(5)
        moviegoupiaopage.validbeijing()
        time.sleep(5)

