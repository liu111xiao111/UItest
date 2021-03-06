# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.bp.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.commodityManagementPage import CommodityManagement
from cases.logger import logger


class XianShiQiangGouXiangXi(TestCase):
    '''
    商品管理,限时抢购,限时抢购详细检查
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
        commodityManagement = CommodityManagement(self, self.driver, self.logger)

        homePage.validSelf()

        #进入商品管理
        commodityManagement.enterCommodityManagementModule()
        #检查待审核,商品详情
        commodityManagement.clickCheckPendingButton()
        commodityManagement.checkCheckPendingItem()

        #检查已经通过,商品详情
        commodityManagement.clickPassingButton()
        commodityManagement.checkCheckPassingItem()




    def tearDown(self):
        self.driver.quit()