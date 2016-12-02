# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.shanghu.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.orderFormManagementPage import OrderFormManagementPage


class QuanBuDingDanZhuangTai(TestCase):
    '''
    全部订单状态检查
    '''
    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId_sh, IDC.udid).getDriver()

        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()


    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        orderFormManagementPage = OrderFormManagementPage(self, self.driver, self.logger)

        homePage.clickOnOrderFormManagement()

        #获取订单信息
        orderFormManagementPage.getOrderInfo()
        orderFormManagementPage.clickFirstItemOfOrderList()

        #检查全部订单信息
        orderFormManagementPage.checkAllOrderDetail(whichcase = "QuanBuDingDan")


    def tearDown(self):
        self.driver.quit()