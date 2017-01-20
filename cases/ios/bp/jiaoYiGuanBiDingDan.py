# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.bp.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.orderFormManagementPage import OrderFormManagementPage
from cases.logger import logger


class JiaoYiGuanBiDingDan(TestCase):
    '''
    交易关闭,订单状态检查
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId_sh,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = Logger()
        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()


    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        orderFormManagementPage = OrderFormManagementPage(self, self.driver, self.logger)

        homePage.clickOnOrderFormManagement()

        #切换到交易关闭订单
        orderFormManagementPage.clickAllOrderStatusButton()
        orderFormManagementPage.clickTradingClosedButton()

        #获取订单信息
        orderFormManagementPage.getOrderInfo()
        orderFormManagementPage.clickFirstItemOfOrderList()

        #检查全部订单信息
        orderFormManagementPage.checkAllOrderDetail()

    def tearDown(self):
        self.driver.quit()