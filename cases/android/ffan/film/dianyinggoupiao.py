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
from cases.android.ffan.film.movieReyingPurchaseSeat_page import dianyingReyingGoupiaoSeat_page


from cases.android.ffan.film.movie_goupiao_page import Moviegoupiaopage
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
        moviegoupiaopage = Moviegoupiaopage(self , self.driver , self.logger)
        dianyingReyingGoupiaoSeatpage= dianyingReyingGoupiaoSeat_page(self , self.driver , self.logger)
        dashboardPage.validSelf()
        moviegoupiaopage.clickchengshi()
        time.sleep(5)
        moviegoupiaopage.inputchengshi()
        time.sleep(5)
        moviegoupiaopage.clickonbaotoushi()
        time.sleep(5)
        dashboardPage.clickOnMovie()
        time.sleep(5)
        moviegoupiaopage.clickOnyingpian()
        time.sleep(5)
        moviegoupiaopage.clickonpingpai()
        time.sleep(5)
        moviegoupiaopage.clickonqita()
        time.sleep(5)
        moviegoupiaopage.clickonquanyeyingyuan()
        time.sleep(5)
        moviegoupiaopage.clickOnbuy()
        time.sleep(5)
        dianyingReyingGoupiaoSeatpage.validSeat()
        time.sleep(5)
        dianyingReyingGoupiaoSeatpage.clickSeatSubmit()
        time.sleep(5)
        moviegoupiaopage.clicktijaiodingdan()
        time.sleep(5)
        moviegoupiaopage.validSelf()
        time.sleep(5)
