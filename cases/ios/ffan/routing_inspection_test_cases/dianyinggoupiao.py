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
from pages.ios.ffan.dianyinggoupiaopage import dianyinggoupiaopage
from cases.logger import logger


class DianYingTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #6
    自动化测试 #6
    首页进入电影模块，检查数据正常并可以成功选座下单，支付并退票
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dianyinggoupiao = dianyinggoupiaopage(self , self.driver , self.logger)
        time.sleep(5)
        dianyinggoupiao.clickOnqiehuanchengshi()
        time.sleep(5)
        dianyinggoupiao.inputchengshi()
        time.sleep(5)
        dianyinggoupiao.clickOnbaotoushi()
        time.sleep(5)
        dashboardPage.clickOnMovie()
        time.sleep(5)
        dianyinggoupiao.clickOnxuanzuo()
        time.sleep(5)
        dianyinggoupiao.clickOnyingcheng()
        time.sleep(5)
