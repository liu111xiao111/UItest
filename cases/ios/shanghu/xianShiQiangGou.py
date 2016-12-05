# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.shanghu.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.commodityManagementPage import CommodityManagement


class XianShiQiangGouXiangXi(TestCase):
    '''
    商品管理,限时抢购,限时抢购详细检查
    '''
    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId_sh, IDC.udid).getDriver()

        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()


    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        commodityManagement = CommodityManagement(self, self.driver, self.logger)

        commodityManagement.enterCommodityManagementModule()
        #检查待审核,商品详情
        commodityManagement.clickCheckPendingButton()
        commodityManagement.checkCheckPendingItem()

        #检查已经通过,商品详情
        commodityManagement.clickPassingButton()
        commodityManagement.checkCheckPassingItem()




    def tearDown(self):
        self.driver.quit()